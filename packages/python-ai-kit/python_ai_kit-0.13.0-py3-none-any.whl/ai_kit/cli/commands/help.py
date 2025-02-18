from pathlib import Path
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.markdown import Markdown
from ai_kit.config import LiteLLMConfig
from ai_kit.shared_console import shared_console
from ai_kit.utils.fs import find_workspace_root
import os

def help_command() -> None:
    """Display AI Kit help information and setup requirements."""
    shared_console.print()
    
    # Create main title
    shared_console.print("[bold cyan]AI Kit Help[/bold cyan]")
    shared_console.print()
    
    # Show current working directory
    shared_console.print(f"[yellow]Current directory:[/yellow] [white]{os.getcwd()}[/white]")

    # Show API Keys Status
    table = Table(
        title="🔑 Required API Keys",
        title_style="bold cyan",
        show_header=False,
        box=None,
        padding=(0, 1)
    )
    table.add_column("Key", style="bold blue")
    table.add_column("Value", style="white")
    table.add_column("Link", style="white")
    
    for key in LiteLLMConfig.required_api_keys():
        value = os.getenv(key)
        has_key = value is not None
        status_style = "green" if has_key else "red"
        status_icon = "✓" if has_key else "✗"
        url = LiteLLMConfig.API_KEY_URLS.get(key, "#")
        link_text = f"[white link={url}]{url}[/]" if url != "#" else ""
        table.add_row(
            f"  {key}",
            Text(
                f"{status_icon} {'configured' if has_key else 'not set'}", 
                style=status_style
            ),
            link_text
        )

    shared_console.print(table)
    shared_console.print()

    # Check for cursor rules
    try:
        workspace_root = find_workspace_root()
        cursor_rules_path = workspace_root / ".cursor" / "rules" / "agent.mdc"
        has_cursor_rules = cursor_rules_path.exists()
        
        status_icon = "✓" if has_cursor_rules else "✗"
        status_style = "green" if has_cursor_rules else "red"
        
        shared_console.print("[bold cyan]System Prompt Status[/bold cyan]")
        shared_console.print(f"[{status_style}]{status_icon} Cursor rules {'found' if has_cursor_rules else 'not found'} at:[/{status_style}]")
        shared_console.print(f"[white]{cursor_rules_path}[/white]")
        shared_console.print()
    except Exception:
        shared_console.print("[bold red]✗ Could not verify cursor rules location[/bold red]")
        shared_console.print("[white]Make sure you're in a valid workspace directory.[/white]")
        shared_console.print()

    # Setup Instructions
    shared_console.print("[bold cyan]Quick Setup Guide[/bold cyan]")
    shared_console.print()
    
    shared_console.print("[bold blue]1.[/bold blue] [yellow]Initialize AI Kit:[/yellow]")
    shared_console.print("   ai-kit init")
    shared_console.print("   This will create the necessary [white].cursor/rules[/white] directory and system prompt.")
    shared_console.print()
    
    shared_console.print("[bold blue]2.[/bold blue] [yellow]Configure API Keys:[/yellow]")
    shared_console.print("   Add the required API keys shown above to your [white].env[/white] file.")
    shared_console.print()
    
    shared_console.print("[bold blue]3.[/bold blue] [yellow]Verify Setup:[/yellow]")
    shared_console.print("   ai-kit help")
    shared_console.print("   Run this command again to verify all requirements are met.")
    shared_console.print()
    
    shared_console.print("AI Kit is now ready to enhance your AI agent's capabilities with web search, thinking, and more!")
    shared_console.print() 