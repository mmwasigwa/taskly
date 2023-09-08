# taskly/commands/start_timer.py

import click
from taskly.models import Task, Timer, session
from datetime import datetime

@click.command()
@click.argument("task_id", type=int)
def start_timer(task_id):
    """Start a timer for a task"""
    task = session.query(Task).filter(Task.id == task_id).first()

    if not task:
        click.echo(f"No task found with ID {task_id}")
        return

    timer = Timer(start_time=datetime.now(), task=task)
    session.add(timer)
    session.commit()

    click.echo(f"Started timer for task: {task.title}")
