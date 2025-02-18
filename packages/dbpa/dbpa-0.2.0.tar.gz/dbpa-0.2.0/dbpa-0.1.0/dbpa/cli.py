"""
Command-line interface for DBPA.
"""
import click
from dbpa.app import DatabaseAssistant


@click.group()
def cli():
    """Database Personal Assistant CLI."""
    pass


@cli.command()
@click.option("--port", default=8501, help="Port to run the web interface on")
@click.option("--config", default=None, help="Path to config file")
def start(port: int, config: str):
    """Start the DBPA web interface."""
    assistant = DatabaseAssistant(config_path=config)
    assistant.run(port=port)


@cli.command()
@click.argument("query")
@click.option("--config", default=None, help="Path to config file")
def query(query: str, config: str):
    """Execute a natural language query."""
    assistant = DatabaseAssistant(config_path=config)
    result = assistant.query(query)
    click.echo(result)


def main():
    """Main entry point for the CLI."""
    cli()
