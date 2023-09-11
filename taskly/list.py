# taskly/commands/list.py

import click
from taskly.models import Task, session

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
