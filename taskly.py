#!/usr/bin/env python
# taskly.py

import click
from colorama import Fore, Style
from models import Category, Task, session

@click.group()
def taskly():
    """Welcome to Taskly - Your Task Manager with in-built Timer"""
    click.echo(Fore.GREEN + "Taskly - Your Task Manager with in-built Timer")
    click.echo(Style.RESET_ALL)

@taskly.command()
@click.argument("category_name")
def add_category(category_name):
    """Add a new category"""
    category = Category(name=category_name)
    session.add(category)
    session.commit()
    click.echo(Fore.CYAN + f"Added category: {category_name}")
    click.echo(Style.RESET_ALL)

@taskly.command()
@click.argument("task_title")
@click.argument("category_name")
def add_task(task_title, category_name):
    """Add a new task"""
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        task = Task(title=task_title, category=category)
        session.add(task)
        session.commit()
        click.echo(Fore.CYAN + f"Added task: {task_title}")
        click.echo(Style.RESET_ALL)
    else:
        click.echo(Fore.RED + f"Category '{category_name}' does not exist.")
        click.echo(Style.RESET_ALL)

@taskly.command()
def list_tasks():
    """List all tasks"""
    tasks = session.query(Task).all()
    if tasks:
        click.echo(Fore.YELLOW + "List of tasks:")
        for task in tasks:
            click.echo(f"{task.id}. {task.title} (Category: {task.category.name})")
        click.echo(Style.RESET_ALL)
    else:
        click.echo(Fore.YELLOW + "No tasks found.")
        click.echo(Style.RESET_ALL)

if __name__ == "__main__":
    taskly()
