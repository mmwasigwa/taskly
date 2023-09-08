# cli.py
import click
from colorama import Fore, Style
from taskly.models import Session, Category, Task

@click.group()
def taskly():
    """Welcome to Taskly - Your Task Manager with in-built Timer"""
    click.echo(Fore.GREEN + "Taskly - Your Task Manager with in-built Timer")
    click.echo(Style.RESET_ALL)

# ... (Your command functions go here)

if __name__ == "__main__":
    taskly()
