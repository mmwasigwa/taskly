# taskly/commands/add.py

import click
from taskly.models import Task, session

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
