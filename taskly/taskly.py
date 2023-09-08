#!/usr/bin/env python

from audioop import add
import click
from colorama import Fore, Style
from taskly.commands.list import list_tasks
from taskly.commands.start_timer import start_timer
from taskly.commands.stop_timer import stop_timer
from taskly.models import Base, engine
from taskly.models import Base, engine  # noqa: F811

Base.metadata.create_all(engine)

@click.group()
def taskly():
    """Welcome to Taskly - Your Task Manager with in-built Timer"""
    click.echo(Fore.GREEN + "Taskly - Your Task Manager with in-built Timer")
    click.echo(Style.RESET_ALL)

# Register the commands
taskly.add_command(add.add)  # noqa: F821
taskly.add_command(list_tasks.list_tasks)  # noqa: F821
taskly.add_command(start_timer.start_timer)  # noqa: F821
taskly.add_command(stop_timer.stop_timer)  # noqa: F821

if __name__ == "__main__":
    taskly()

