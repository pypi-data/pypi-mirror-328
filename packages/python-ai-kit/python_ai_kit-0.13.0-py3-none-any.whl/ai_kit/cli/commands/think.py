from ai_kit.cli.registry import registry_instance
from time import perf_counter
from typing import List, Dict
from ai_kit.core.router import Router, RouteRegistry, RouteDefinition
from ai_kit.utils import print_stream
from ai_kit.utils.fs import package_root, load_system_prompt
from ai_kit.core.llms.litellm_client import ReasoningClient
from ai_kit.core.llms.deepseek_client import DeepSeekClient
from ai_kit.core.llms.together_client import TogetherClient
from ai_kit.core.llms.groq_client import GroqClient
from ai_kit.shared_console import shared_console
from ai_kit.core.prompt_loader import PromptLoader

# Constants
PACKAGE_ROOT = package_root()

# we load think from the package root (since its a system prompt)
THINK_PROMPT_PATH = f"{PACKAGE_ROOT}/system_prompts/think.md"

THINK_ROUTER_PROMPT = """
Your job is to route between three options:

# Nothink
For simple requests that don't require any thinking. This includes conversaion, simple math and coding tasks.

# Think
For most tasks, general coding tasks, and tasks that don't require deep thinking. This includes general coding tasks, tasks that are procedurally complex, and tasks that don't require deep reasoning. Use this most of the time

# Deepthink
For advanced reasoning, highly advanced coding, and tasks requiring deep analysis. This includes complex coding tasks across a codebase, reasoning, and complex problem solving. This should be used only for the most complex tasks like difficult debugging tasks, difficult code generation tasks, and difficult reasoning tasks.
"""


class ThinkHandler:
    def __init__(
        self,
        think_model: str = "r1-70b",
        deepthink_model: str = "r1-together",
    ):
        self.think_client = self._get_think_client(think_model)
        self.deepthink_client = self._get_deepthink_client(deepthink_model)
        self.router = Router(
            route_registry=self._register_routes(), model="gemini-2.0-flash"
        )

    def _get_think_client(self, model: str):
        if model == "r1-70b":
            return GroqClient(model=model)
        else:
            raise ValueError(f"Unsupported model for thinking: {model}")

    def _get_deepthink_client(self, model: str):
        if model == "r1-together":
            return TogetherClient(model=model)
        elif model == "r1":
            return DeepSeekClient(model=model)
        else:
            return ReasoningClient(model=model)

    def _register_routes(self) -> RouteRegistry:
        """Setup available routes with their conditions."""
        registry = RouteRegistry()
        registry.register(
            RouteDefinition(
                name="deepthink",
                description="Advanced reasoning, highly advanced coding, and tasks requiring deep analysis.",
            )
        )

        registry.register(
            RouteDefinition(
                name="think",
                description="Most tasks, general coding tasks, and tasks that don't require deep thinking.",
            )
        )

        registry.register(
            RouteDefinition(
                name="nothink",
                description="Extremely simple conversation that doesn't need any thinking..",
            )
        )

        registry.register(
            RouteDefinition(
                name="fallback",
                description="Fallback route if no other route is a good match.",
            )
        )
        return registry

    async def handle_think(self, prompt: str):
        """Call the router to determine the best route for the prompt."""
        s = perf_counter()
        with shared_console.status("[bold yellow]Routing..."):
            decision = self.router.route(prompt)
            e = perf_counter()
        shared_console.print(
            f"[yellow]Routed to: [bold blue]{decision.route}[/bold blue] using [bold green]{self.router.client.mapped_model}[/bold green] in [bold yellow]{e - s:0.2f}[/bold yellow] seconds. [/yellow]"
        )
        if decision.route == "deepthink":
            await self._handle_deepthink(prompt)
        elif decision.route == "think":
            await self._handle_think(prompt)
        elif decision.route == "nothink":
            self._handle_nothink()
        else:  # fallback
            await self._handle_think()

    def _build_system_prompt(self) -> str:
        """Construct the system prompt with dynamic content."""
        try:
            base_prompt = load_system_prompt(THINK_PROMPT_PATH)
        except FileNotFoundError:
            shared_console.print(
                f"[red]Error:[/] Could not find think.md prompt file at {THINK_PROMPT_PATH}"
            )
            shared_console.print(
                "[yellow]Hint:[/] Make sure you have initialized ai-kit with `ai-kit init`"
            )
            raise SystemExit(1)

        return (
            base_prompt.format(commands=registry_instance.markdown_prompt)
            + "\n\n"
            + THINK_ROUTER_PROMPT
        )

    async def get_messages(self, prompt: str) -> List[Dict[str, str]]:
        prompt_loader = PromptLoader()
        processed_prompt = await prompt_loader.load(prompt)
        system_prompt = self._build_system_prompt()
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": processed_prompt},
        ]
        return messages

    async def _handle_deepthink(self, prompt: str) -> None:
        """Handle requests requiring deep thinking."""
        s = perf_counter()
        with shared_console.status("[bold green]Thinking Deeply..."):
            shared_console.print(
                f"[yellow]Using model: [bold green]{self.deepthink_client.mapped_model}[/bold green][/yellow]"
            )
            messages = await self.get_messages(prompt)
            response = await self.deepthink_client.reasoning_completion(
                messages=messages,
                stream=True,
                thoughts_only=True,
            )
            shared_console.print("\n[bold]Thinking Process:[/bold]")
            await print_stream(response)
        e = perf_counter()
        shared_console.print(f"[yellow]Thought for {e - s:0.2f} seconds.[/yellow]")

    async def _handle_think(self, prompt: str) -> None:
        """Handle requests requiring deep thinking."""
        s = perf_counter()
        with shared_console.status("[bold green]Thinking..."):
            shared_console.print(
                f"[yellow]Using model: [bold green]{self.think_client.mapped_model}[/bold green][/yellow]"
            )
            messages = await self.get_messages(prompt)
            response = await self.think_client.reasoning_completion(
                messages=messages,
                stream=True,
                thoughts_only=True,
            )
            await print_stream(response)
        e = perf_counter()
        shared_console.print(f"[yellow]Thought for {e - s:0.2f} seconds.[/yellow]")

    def _handle_nothink(self):
        """Handle simple requests that don't require deep thinking."""
        shared_console.print(f"[yellow]Using model: [bold green]nothink[/bold green][/yellow]")
        shared_console.print(f"<thinking>I should answer the user's request</thinking>")


async def think_command(prompt: str, think_model: str, deepthink_model: str):
    """CLI entry point for the think command."""
    handler = ThinkHandler(
        think_model=think_model,
        deepthink_model=deepthink_model,
    )
    await handler.handle_think(prompt)
