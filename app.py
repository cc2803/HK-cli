import click
import importlib
import pkgutil
import commands  # This is your commands/ folder as a package


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
