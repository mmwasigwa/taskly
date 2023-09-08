#!/usr/bin/env python

import click
from colorama import Fore, Style
import time

# Our dictionary to store task timers
task_timers = {}

@click.command()
def taskly():
    """Welcome to Taskly - Your Task Manager with in-built Timer"""
    click.echo(Fore.GREEN + "Taskly - Your Task Manager with in-built Timer")
    click.echo(Style.RESET_ALL)


@click.argument("task_name")
def add(task_name):
    """Add a new task"""
    # Implement task addition logic here
    click.echo(f"Added task: {task_name}")

def show():
    """List all tasks"""
    # Implement task listing logic here
    click.echo("List of tasks:")

# Timer


@click.argument("task_name")
def stop(task_name):
    """Stop a task timer"""
    if task_name in task_timers:
        elapsed_time = time.time() - task_timers[task_name]
        click.echo(f"Stopped timer for task: {task_name}")
        click.echo(f"Elapsed time: {elapsed_time:.2f} seconds")
        del task_timers[task_name]
    else:
        click.echo(f"Task '{task_name}' timer is not running.")

if __name__ == "__main__":
    taskly()