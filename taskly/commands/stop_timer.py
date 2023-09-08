# taskly/commands/stop_timer.py

import click
from taskly.models import Timer, session
from datetime import datetime

@click.command()
@click.argument("timer_id", type=int)
def stop_timer(timer_id):
    """Stop a timer for a task"""
    timer = session.query(Timer).filter(Timer.id == timer_id).first()

    if not timer:
        click.echo(f"No timer found with ID {timer_id}")
        return

    timer.end_time = datetime.now()
    session.commit()

    click.echo(f"Stopped timer for task: {timer.task.title}")
