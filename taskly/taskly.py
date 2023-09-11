#!/usr/bin/env python

import click
from colorama import Fore, Style
from models import Base, engine, Task, session

Base.metadata.create_all(engine)

@click.group()
def taskly():
    """Taskly - Task Manager with Timer"""
    click.echo(Fore.GREEN + "Taskly - Task Manager with Timer")
    click.echo(Style.RESET_ALL)

@click.command()
@click.argument("title")
@click.option("--description", default="", help="Task description (optional)")
@click.option("--category", help="Task category (optional)")
def add(title, description, category):
    """Add a new task"""
    task = Task(title=title, description=description)

    if category:
        task.category = category

    session.add(task)
    session.commit()

    click.echo(f"Added task: {title}")

@click.command()
def list_tasks():
    """List all tasks"""
    tasks = session.query(Task).all()
    if tasks:
        click.echo("List of tasks:")
        for task in tasks:
            click.echo(f"{task.id}. {task.title}")
    else:
        click.echo("No tasks found.")

# Register the commands
taskly.add_command(add)
taskly.add_command(list_tasks)

if __name__ == "__main__":
    taskly()