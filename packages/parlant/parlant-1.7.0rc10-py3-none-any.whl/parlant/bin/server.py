# Copyright 2024 Emcie Co Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# mypy: disable-error-code=import-untyped

import asyncio
from contextlib import asynccontextmanager, AsyncExitStack
from dataclasses import dataclass
import importlib
import json
import os
import traceback
from lagom import Container, Singleton
from typing import AsyncIterator, Callable, Iterable, cast
import toml
from typing_extensions import NoReturn
import click
import click_completion
from pathlib import Path
import sys
import uvicorn

from parlant.adapters.db.transient import TransientDocumentDatabase
from parlant.adapters.loggers.websocket import WebSocketLogger
from parlant.adapters.vector_db.chroma import ChromaDatabase
from parlant.core.engines.alpha import guideline_proposer
from parlant.core.engines.alpha import tool_caller
from parlant.core.engines.alpha import fluid_message_generator
from parlant.core.engines.alpha.hooks import LifecycleHooks
from parlant.core.engines.alpha.message_assembler import AssembledMessageSchema
from parlant.core.fragments import FragmentDocumentStore, FragmentStore
from parlant.core.nlp.service import NLPService
from parlant.core.persistence.common import MigrationRequired
from parlant.core.shots import ShotCollection
from parlant.core.tags import TagDocumentStore, TagStore
from parlant.api.app import create_api_app, ASGIApplication
from parlant.core.background_tasks import BackgroundTaskService
from parlant.core.contextual_correlator import ContextualCorrelator
from parlant.core.agents import AgentDocumentStore, AgentStore
from parlant.core.context_variables import ContextVariableDocumentStore, ContextVariableStore
from parlant.core.emission.event_publisher import EventPublisherFactory
from parlant.core.emissions import EventEmitterFactory
from parlant.core.customers import CustomerDocumentStore, CustomerStore
from parlant.core.evaluations import (
    EvaluationListener,
    PollingEvaluationListener,
    EvaluationDocumentStore,
    EvaluationStatus,
    EvaluationStore,
)
from parlant.core.guideline_connections import (
    GuidelineConnectionDocumentStore,
    GuidelineConnectionStore,
)
from parlant.core.guidelines import (
    GuidelineDocumentStore,
    GuidelineStore,
)
from parlant.adapters.db.json_file import JSONFileDocumentDatabase
from parlant.core.nlp.embedding import EmbedderFactory
from parlant.core.nlp.generation import SchematicGenerator
from parlant.core.services.tools.service_registry import (
    ServiceRegistry,
    ServiceDocumentRegistry,
)
from parlant.core.sessions import (
    PollingSessionListener,
    SessionDocumentStore,
    SessionListener,
    SessionStore,
)
from parlant.core.glossary import GlossaryStore, GlossaryVectorStore
from parlant.core.engines.alpha.engine import AlphaEngine
from parlant.core.guideline_tool_associations import (
    GuidelineToolAssociationDocumentStore,
    GuidelineToolAssociationStore,
)
from parlant.core.engines.alpha.tool_caller import ToolCallInferenceSchema, ToolCallerInferenceShot
from parlant.core.engines.alpha.guideline_proposer import (
    GuidelineProposer,
    GuidelinePropositionShot,
    GuidelinePropositionsSchema,
)
from parlant.core.engines.alpha.fluid_message_generator import (
    FluidMessageGenerator,
    FluidMessageGeneratorShot,
    FluidMessageSchema,
)
from parlant.core.engines.alpha.tool_event_generator import ToolEventGenerator
from parlant.core.engines.types import Engine
from parlant.core.services.indexing.behavioral_change_evaluation import (
    BehavioralChangeEvaluator,
)
from parlant.core.services.indexing.coherence_checker import (
    CoherenceChecker,
    ConditionsEntailmentTestsSchema,
    ActionsContradictionTestsSchema,
)
from parlant.core.services.indexing.guideline_connection_proposer import (
    GuidelineConnectionProposer,
    GuidelineConnectionPropositionsSchema,
)
from parlant.core.loggers import CompositeLogger, FileLogger, LogLevel, Logger
from parlant.core.application import Application
from parlant.core.version import VERSION

DEFAULT_PORT = 8800
SERVER_ADDRESS = "https://localhost"

DEFAULT_NLP_SERVICE = "openai"

DEFAULT_HOME_DIR = "runtime-data" if Path("runtime-data").exists() else "parlant-data"
PARLANT_HOME_DIR = Path(os.environ.get("PARLANT_HOME", DEFAULT_HOME_DIR))
PARLANT_HOME_DIR.mkdir(parents=True, exist_ok=True)

EXIT_STACK: AsyncExitStack

DEFAULT_AGENT_NAME = "Default Agent"

sys.path.append(PARLANT_HOME_DIR.as_posix())
sys.path.append(".")

CORRELATOR = ContextualCorrelator()

LOGGER = FileLogger(PARLANT_HOME_DIR / "parlant.log", CORRELATOR, LogLevel.INFO)

BACKGROUND_TASK_SERVICE = BackgroundTaskService(LOGGER)


class StartupError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


@dataclass
class CLIParams:
    port: int
    nlp_service: str
    log_level: str
    modules: list[str]
    migrate: bool


def load_nlp_service(name: str, extra_name: str, class_name: str, module_path: str) -> NLPService:
    try:
        module = importlib.import_module(module_path)
        service = getattr(module, class_name)
        return cast(NLPService, service(LOGGER))
    except ModuleNotFoundError as exc:
        LOGGER.error(f"Failed to import module: {exc.name}")
        LOGGER.critical(
            f"{name} support is not installed. Please install it with: pip install parlant[{extra_name}]."
        )
        sys.exit(1)


def load_anthropic() -> NLPService:
    return load_nlp_service(
        "Anthropic", "anthropic", "AnthropicService", "parlant.adapters.nlp.anthropic"
    )


def load_aws() -> NLPService:
    return load_nlp_service("AWS", "aws", "BedrockService", "parlant.adapters.nlp.aws")


def load_azure() -> NLPService:
    from parlant.adapters.nlp.azure_service import AzureService

    return AzureService(LOGGER)


def load_cerebras() -> NLPService:
    return load_nlp_service(
        "Cerebras", "cerebras", "CerebrasService", "parlant.adapters.nlp.cerebras"
    )


def load_deepseek() -> NLPService:
    return load_nlp_service(
        "DeepSeek", "deepseek", "DeepSeekService", "parlant.adapters.nlp.deepseek"
    )


def load_gemini() -> NLPService:
    return load_nlp_service("Gemini", "gemini", "GeminiService", "parlant.adapters.nlp.gemini")


def load_openai() -> NLPService:
    from parlant.adapters.nlp.openai_service import OpenAIService

    return OpenAIService(LOGGER)


def load_together() -> NLPService:
    return load_nlp_service(
        "Together.ai", "together", "TogetherService", "parlant.adapters.nlp.together"
    )


async def create_agent_if_absent(agent_store: AgentStore) -> None:
    agents = await agent_store.list_agents()
    if not agents:
        await agent_store.create_agent(name=DEFAULT_AGENT_NAME)


async def get_module_list_from_config() -> list[str]:
    config_file = Path("parlant.toml")

    if config_file.exists():
        config = toml.load(config_file)
        # Expecting structure of:
        # [parlant]
        # modules = ["module_1", "module_2"]
        return list(config.get("parlant", {}).get("modules", []))

    return []


@asynccontextmanager
async def load_modules(
    container: Container,
    modules: Iterable[str],
) -> AsyncIterator[Container]:
    imported_modules = []

    for module_path in modules:
        module = importlib.import_module(module_path)
        if not hasattr(module, "initialize_module") or not hasattr(module, "shutdown_module"):
            raise StartupError(
                f"Module '{module.__name__}' must define initialize_module(container: lagom.Container) and shutdown_module()"
            )
        imported_modules.append(module)

    for m in imported_modules:
        LOGGER.info(f"Initializing module '{m.__name__}'")

        if new_container := await m.initialize_module(container):
            container = new_container

    try:
        yield container
    finally:
        for m in reversed(imported_modules):
            LOGGER.info(f"Shutting down module '{m.__name__}'")
            await m.shutdown_module()


@asynccontextmanager
async def setup_container(
    nlp_service_name: str,
    log_level: str,
    migrate: bool,
) -> AsyncIterator[Container]:
    c = Container()

    c[BackgroundTaskService] = await EXIT_STACK.enter_async_context(BACKGROUND_TASK_SERVICE)

    c[ContextualCorrelator] = CORRELATOR

    c[WebSocketLogger] = WebSocketLogger(CORRELATOR, LogLevel.INFO)
    c[Logger] = CompositeLogger(
        [
            LOGGER,
            c[WebSocketLogger],
        ]
    )
    c[Logger].set_level(
        {
            "info": LogLevel.INFO,
            "debug": LogLevel.DEBUG,
            "warning": LogLevel.WARNING,
            "error": LogLevel.ERROR,
            "critical": LogLevel.CRITICAL,
        }[log_level],
    )
    await c[BackgroundTaskService].start(c[WebSocketLogger].start(), tag="websocket-logger")

    agents_db = await EXIT_STACK.enter_async_context(
        JSONFileDocumentDatabase(LOGGER, PARLANT_HOME_DIR / "agents.json")
    )
    context_variables_db = await EXIT_STACK.enter_async_context(
        JSONFileDocumentDatabase(LOGGER, PARLANT_HOME_DIR / "context_variables.json")
    )
    tags_db = await EXIT_STACK.enter_async_context(
        JSONFileDocumentDatabase(LOGGER, PARLANT_HOME_DIR / "tags.json")
    )
    customers_db = await EXIT_STACK.enter_async_context(
        JSONFileDocumentDatabase(LOGGER, PARLANT_HOME_DIR / "customers.json")
    )
    sessions_db = await EXIT_STACK.enter_async_context(
        JSONFileDocumentDatabase(LOGGER, PARLANT_HOME_DIR / "sessions.json")
    )
    guidelines_db = await EXIT_STACK.enter_async_context(
        JSONFileDocumentDatabase(LOGGER, PARLANT_HOME_DIR / "guidelines.json")
    )
    guideline_tool_associations_db = await EXIT_STACK.enter_async_context(
        JSONFileDocumentDatabase(LOGGER, PARLANT_HOME_DIR / "guideline_tool_associations.json")
    )
    guideline_connections_db = await EXIT_STACK.enter_async_context(
        JSONFileDocumentDatabase(LOGGER, PARLANT_HOME_DIR / "guideline_connections.json")
    )
    evaluations_db = await EXIT_STACK.enter_async_context(
        JSONFileDocumentDatabase(LOGGER, PARLANT_HOME_DIR / "evaluations.json")
    )
    services_db = await EXIT_STACK.enter_async_context(
        JSONFileDocumentDatabase(LOGGER, PARLANT_HOME_DIR / "services.json")
    )

    try:
        c[AgentStore] = await EXIT_STACK.enter_async_context(AgentDocumentStore(agents_db, migrate))
        c[ContextVariableStore] = await EXIT_STACK.enter_async_context(
            ContextVariableDocumentStore(context_variables_db)
        )
        c[TagStore] = await EXIT_STACK.enter_async_context(TagDocumentStore(tags_db, migrate))
        c[CustomerStore] = await EXIT_STACK.enter_async_context(
            CustomerDocumentStore(customers_db, migrate)
        )
        c[FragmentStore] = await EXIT_STACK.enter_async_context(
            FragmentDocumentStore(TransientDocumentDatabase())
        )
        c[GuidelineStore] = await EXIT_STACK.enter_async_context(
            GuidelineDocumentStore(guidelines_db, migrate)
        )
        c[GuidelineToolAssociationStore] = await EXIT_STACK.enter_async_context(
            GuidelineToolAssociationDocumentStore(guideline_tool_associations_db, migrate)
        )
        c[GuidelineConnectionStore] = await EXIT_STACK.enter_async_context(
            GuidelineConnectionDocumentStore(guideline_connections_db, migrate)
        )
        c[SessionStore] = await EXIT_STACK.enter_async_context(
            SessionDocumentStore(sessions_db, migrate)
        )
        c[SessionListener] = PollingSessionListener

        c[EvaluationStore] = await EXIT_STACK.enter_async_context(
            EvaluationDocumentStore(evaluations_db, migrate)
        )
        c[EvaluationListener] = PollingEvaluationListener

        c[EventEmitterFactory] = Singleton(EventPublisherFactory)

        nlp_service_initializer: dict[str, Callable[[], NLPService]] = {
            "anthropic": load_anthropic,
            "aws": load_aws,
            "azure": load_azure,
            "cerebras": load_cerebras,
            "deepseek": load_deepseek,
            "gemini": load_gemini,
            "openai": load_openai,
            "together": load_together,
        }

        c[ServiceRegistry] = await EXIT_STACK.enter_async_context(
            ServiceDocumentRegistry(
                database=services_db,
                event_emitter_factory=c[EventEmitterFactory],
                correlator=c[ContextualCorrelator],
                nlp_services={nlp_service_name: nlp_service_initializer[nlp_service_name]()},
                logger=c[Logger],
                allow_migration=migrate,
            )
        )

        nlp_service = await c[ServiceRegistry].read_nlp_service(nlp_service_name)

        c[NLPService] = nlp_service

        embedder_factory = EmbedderFactory(c)
        c[GlossaryStore] = await EXIT_STACK.enter_async_context(
            GlossaryVectorStore(
                await EXIT_STACK.enter_async_context(
                    ChromaDatabase(LOGGER, PARLANT_HOME_DIR, embedder_factory),
                ),
                embedder_type=type(await nlp_service.get_embedder()),
                embedder_factory=embedder_factory,
            )
        )
    except MigrationRequired as e:
        c[Logger].critical(str(e))
        die("Please re-run with `--migrate` to migrate your data to the new version.")
        sys.exit(1)

    c[SchematicGenerator[GuidelinePropositionsSchema]] = await nlp_service.get_schematic_generator(
        GuidelinePropositionsSchema
    )
    c[SchematicGenerator[FluidMessageSchema]] = await nlp_service.get_schematic_generator(
        FluidMessageSchema
    )
    c[SchematicGenerator[AssembledMessageSchema]] = await nlp_service.get_schematic_generator(
        AssembledMessageSchema
    )
    c[SchematicGenerator[ToolCallInferenceSchema]] = await nlp_service.get_schematic_generator(
        ToolCallInferenceSchema
    )
    c[
        SchematicGenerator[ConditionsEntailmentTestsSchema]
    ] = await nlp_service.get_schematic_generator(ConditionsEntailmentTestsSchema)
    c[
        SchematicGenerator[ActionsContradictionTestsSchema]
    ] = await nlp_service.get_schematic_generator(ActionsContradictionTestsSchema)
    c[
        SchematicGenerator[GuidelineConnectionPropositionsSchema]
    ] = await nlp_service.get_schematic_generator(GuidelineConnectionPropositionsSchema)

    c[ShotCollection[GuidelinePropositionShot]] = guideline_proposer.shot_collection
    c[ShotCollection[ToolCallerInferenceShot]] = tool_caller.shot_collection
    c[ShotCollection[FluidMessageGeneratorShot]] = fluid_message_generator.shot_collection

    c[LifecycleHooks] = LifecycleHooks()

    c[GuidelineProposer] = GuidelineProposer(
        c[Logger],
        c[SchematicGenerator[GuidelinePropositionsSchema]],
    )
    c[GuidelineConnectionProposer] = GuidelineConnectionProposer(
        c[Logger],
        c[SchematicGenerator[GuidelineConnectionPropositionsSchema]],
        c[GlossaryStore],
    )

    c[CoherenceChecker] = CoherenceChecker(
        c[Logger],
        c[SchematicGenerator[ConditionsEntailmentTestsSchema]],
        c[SchematicGenerator[ActionsContradictionTestsSchema]],
        c[GlossaryStore],
    )

    c[BehavioralChangeEvaluator] = BehavioralChangeEvaluator(
        c[Logger],
        c[BackgroundTaskService],
        c[AgentStore],
        c[EvaluationStore],
        c[GuidelineStore],
        c[GuidelineConnectionProposer],
        c[CoherenceChecker],
    )

    c[FluidMessageGenerator] = FluidMessageGenerator(
        c[Logger],
        c[ContextualCorrelator],
        c[SchematicGenerator[FluidMessageSchema]],
    )

    c[ToolEventGenerator] = ToolEventGenerator(
        c[Logger],
        c[ContextualCorrelator],
        c[ServiceRegistry],
        c[SchematicGenerator[ToolCallInferenceSchema]],
    )

    c[Engine] = Singleton(AlphaEngine)

    c[Application] = Application(c)

    yield c


async def recover_server_tasks(
    evaluation_store: EvaluationStore,
    evaluator: BehavioralChangeEvaluator,
) -> None:
    for evaluation in await evaluation_store.list_evaluations():
        if evaluation.status in [EvaluationStatus.PENDING, EvaluationStatus.RUNNING]:
            LOGGER.info(f"Recovering evaluation task: '{evaluation.id}'")
            await evaluator.run_evaluation(evaluation)


def _alert_user_to_migrations_when_upgrading_from_a_version_before_1_7_0() -> None:
    # Check if the system is ready for version >1.7.0
    # Checking if the Parlant server is compatible by examining the agent version
    if (PARLANT_HOME_DIR / "agents.json").exists():
        with open(PARLANT_HOME_DIR / "agents.json", "r") as agents_db:
            raw_data = json.load(agents_db)
            agents = raw_data.get("agents")
            if agents and agents[0].get("version") == "0.1.0":
                die(
                    "You're running a particulary old version of Parlant.\n"
                    "To upgrade your existing data to the new schema version, please run\n"
                    "`parlant-prepare-migration` and then re-run the server with `--migrate`."
                )


@asynccontextmanager
async def load_app(params: CLIParams) -> AsyncIterator[ASGIApplication]:
    # TODO: Deprecate this check in future versions
    _alert_user_to_migrations_when_upgrading_from_a_version_before_1_7_0()

    global EXIT_STACK

    EXIT_STACK = AsyncExitStack()

    async with (
        setup_container(params.nlp_service, params.log_level, params.migrate) as base_container,
        EXIT_STACK,
    ):
        modules = set(await get_module_list_from_config() + params.modules)

        if modules:
            # Allow modules to return a different container
            actual_container = await EXIT_STACK.enter_async_context(
                load_modules(base_container, modules),
            )
        else:
            actual_container = base_container
            LOGGER.info("No external modules selected")

        await recover_server_tasks(
            evaluation_store=actual_container[EvaluationStore],
            evaluator=actual_container[BehavioralChangeEvaluator],
        )

        await create_agent_if_absent(actual_container[AgentStore])

        yield await create_api_app(actual_container)


async def serve_app(
    app: ASGIApplication,
    port: int,
) -> None:
    config = uvicorn.Config(
        app,
        host="0.0.0.0",
        port=port,
        log_level="critical",
        timeout_graceful_shutdown=1,
    )
    server = uvicorn.Server(config)

    try:
        LOGGER.info(".-----------------------------------------.")
        LOGGER.info("| Server is ready for some serious action |")
        LOGGER.info("'-----------------------------------------'")
        LOGGER.info(f"Try the Sandbox UI at http://localhost:{port}")
        await server.serve()
        await asyncio.sleep(0)  # Required to trigger the possible cancellation error
    except (KeyboardInterrupt, asyncio.CancelledError):
        await BACKGROUND_TASK_SERVICE.cancel_all(reason="Server shutting down")
    except BaseException as e:
        LOGGER.critical(traceback.format_exc())
        LOGGER.critical(e.__class__.__name__ + ": " + str(e))
        sys.exit(1)


def die(message: str) -> NoReturn:
    print(message, file=sys.stderr)
    sys.exit(1)


def require_env_keys(keys: list[str]) -> None:
    if missing_keys := [k for k in keys if not os.environ.get(k)]:
        die(f"The following environment variables are missing:\n{', '.join(missing_keys)}")


async def start_server(params: CLIParams) -> None:
    LOGGER.set_level(
        {
            "info": LogLevel.INFO,
            "debug": LogLevel.DEBUG,
            "warning": LogLevel.WARNING,
            "error": LogLevel.ERROR,
            "critical": LogLevel.CRITICAL,
        }[params.log_level],
    )

    LOGGER.info(f"Parlant server version {VERSION}")
    LOGGER.info(f"Using home directory '{PARLANT_HOME_DIR.absolute()}'")

    if "PARLANT_HOME" not in os.environ and DEFAULT_HOME_DIR == "runtime-data":
        LOGGER.warning(
            "'runtime-data' is deprecated as the name of the default PARLANT_HOME directory"
        )
        LOGGER.warning(
            "Please rename 'runtime-data' to 'parlant-data' to avoid this warning in the future."
        )

    async with load_app(params) as app:
        await serve_app(
            app,
            params.port,
        )


def main() -> None:
    click_completion.init()

    @click.group(invoke_without_command=True)
    @click.option(
        "-p",
        "--port",
        type=int,
        default=DEFAULT_PORT,
        help="Server port",
    )
    @click.option(
        "--openai",
        is_flag=True,
        help="Run with OpenAI. The environment variable OPENAI_API_KEY must be set",
        default=True,
    )
    @click.option(
        "--anthropic",
        is_flag=True,
        help="Run with Anthropic. The environment variable ANTHROPIC_API_KEY must be set and install the extra package parlant[anthropic].",
        default=False,
    )
    @click.option(
        "--aws",
        is_flag=True,
        help="Run with AWS Bedrock. The following environment variables must be set: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION and install the extra package parlant[aws].",
        default=False,
    )
    @click.option(
        "--azure",
        is_flag=True,
        help="Run with Azure OpenAI. The following environment variables must be set: AZURE_API_KEY, AZURE_ENDPOINT",
        default=False,
    )
    @click.option(
        "--cerebras",
        is_flag=True,
        help="Run with Cerebras. The environment variable CEREBRAS_API_KEY must be set and install the extra package parlant[cerebras].",
        default=False,
    )
    @click.option(
        "--deepseek",
        is_flag=True,
        help="Run with DeepSeek. You must set the DEEPSEEK_API_KEY environment variable and install the extra package parlant[deepseek].",
        default=False,
    )
    @click.option(
        "--gemini",
        is_flag=True,
        help="Run with Gemini. The environment variable GEMINI_API_KEY must be set and install the extra package parlant[gemini].",
        default=False,
    )
    @click.option(
        "--together",
        is_flag=True,
        help="Run with Together AI. The environment variable TOGETHER_API_KEY must be set and install the extra package parlant[together].",
        default=False,
    )
    @click.option(
        "--log-level",
        type=click.Choice(["debug", "info", "warning", "error", "critical"]),
        default="info",
        help="Log level",
    )
    @click.option(
        "--module",
        multiple=True,
        default=[],
        metavar="MODULE",
        help=(
            "Specify a module to load. To load multiple modules, pass this argument multiple times. "
            "If parlant.toml exists in the working directory, any additional modules specified "
            "in it will also be loaded."
        ),
    )
    @click.option(
        "--version",
        is_flag=True,
        help="Print server version and exit",
    )
    @click.option(
        "--migrate",
        is_flag=True,
        help=(
            "Enable to migrate the database schema to the latest version. "
            "Disable to exit if the database schema is not up-to-date."
        ),
    )
    @click.pass_context
    def cli(
        ctx: click.Context,
        port: int,
        openai: bool,
        aws: bool,
        azure: bool,
        gemini: bool,
        deepseek: bool,
        anthropic: bool,
        cerebras: bool,
        together: bool,
        log_level: str,
        module: tuple[str],
        version: bool,
        migrate: bool,
    ) -> None:
        if version:
            print(f"Parlant v{VERSION}")
            sys.exit(0)

        if sum([openai, aws, azure, deepseek, gemini, anthropic, cerebras, together]) > 2:
            print("error: only one NLP service profile can be selected")
            sys.exit(1)

        non_default_service_selected = any(
            (aws, azure, deepseek, gemini, anthropic, cerebras, together)
        )

        if not non_default_service_selected:
            nlp_service = "openai"
            require_env_keys(["OPENAI_API_KEY"])
        elif aws:
            nlp_service = "aws"
            require_env_keys(["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_REGION"])
        elif azure:
            nlp_service = "azure"
            require_env_keys(["AZURE_API_KEY", "AZURE_ENDPOINT"])
        elif gemini:
            nlp_service = "gemini"
            require_env_keys(["GEMINI_API_KEY"])
        elif deepseek:
            nlp_service = "deepseek"
            require_env_keys(["DEEPSEEK_API_KEY"])
        elif anthropic:
            nlp_service = "anthropic"
            require_env_keys(["ANTHROPIC_API_KEY"])
        elif cerebras:
            nlp_service = "cerebras"
            require_env_keys(["CEREBRAS_API_KEY"])
        elif together:
            nlp_service = "together"
            require_env_keys(["TOGETHER_API_KEY"])
        else:
            assert False, "Should never get here"

        ctx.obj = CLIParams(
            port=port,
            nlp_service=nlp_service,
            log_level=log_level,
            modules=list(module),
            migrate=migrate,
        )

        asyncio.run(start_server(ctx.obj))

    try:
        cli()
    except StartupError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
