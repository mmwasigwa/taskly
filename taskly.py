#!/usr/bin/env python

# taskly.py
import click
from colorama import Fore, Style

@click.command()
def taskly():
    """Welcome to Taskly - Your Task Manager with in-built Timer"""
    click.echo(Fore.GREEN + "Taskly - Your Task Manager with in-built Timer")
    click.echo(Style.RESET_ALL)

@taskly.command()
@click.argument("task_name")
def add(task_name):
    """Add a new task"""
    # Implement task addition logic here
    click.echo(f"Added task: {task_name}")

@taskly.command()
def list():
    """List all tasks"""
    # Implement task listing logic here
    click.echo("List of tasks:")

# Add more commands as needed

if __name__ == "__main__":
    taskly()



