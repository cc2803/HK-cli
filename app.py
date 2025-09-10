import click
import importlib
import os,sys
import pkgutil
import commands  # This is your commands/ folder as a package

# Ensure the project root is in sys.path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

@click.group()
def cli():
    """Hell's Kitchen Trivia CLI."""
    pass


def load_commands():
    """
    Dynamically import all command modules from the commands/ package.
    Looks for a `cli_command` object in each module and adds it to the CLI group.
    """
    for _, module_name, _ in pkgutil.iter_modules(commands.__path__):
        module = importlib.import_module(f"commands.{module_name}")
        if hasattr(module, "cli_command"):
            cli.add_command(module.cli_command)


# Register all commands before starting CLI
load_commands()

if __name__ == "__main__":
    cli()
