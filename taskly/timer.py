#!/usr/bin/env python

import click
from colorama import Fore, Style
from taskly.models import Base, engine
from taskly.list import list_tasks
from taskly.timer import timer  # Import the timer group from timer.py

Base.metadata.create_all(engine)

@click.group()
def taskly():
    """Welcome to Taskly - Your Task Manager with in-built Timer"""
    click.echo(Fore.GREEN + "Taskly - Your Task Manager with in-built Timer")
    click.echo(Style.RESET_ALL)

# Register the commands
taskly.add_command(list_tasks.list_tasks)  # Register your existing list_tasks command
taskly.add_command(timer)  # Register the timer group from timer.py

if __name__ == "__main__":
    taskly()
