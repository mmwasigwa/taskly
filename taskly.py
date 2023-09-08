#!/usr/bin/env python

import click
from colorama import Fore, Style
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define the Category and Task models
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    tasks = relationship("Task", back_populates="category")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="tasks")

engine = create_engine("sqlite:///taskly.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

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

#edit task
@taskly.command()
@click.argument("task_id", type=int)
@click.argument("new_title")
def edit_task(task_id, new_title):
    """Edit the title of a task"""
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        task.title = new_title
        session.commit()
        click.echo(Fore.CYAN + f"Edited task {task_id}: {new_title}")
        click.echo(Style.RESET_ALL)
    else:
        click.echo(Fore.RED + f"Task with ID {task_id} does not exist.")
        click.echo(Style.RESET_ALL)
# Delete tasks
@taskly.command()
@click.argument("task_id", type=int)
def delete_task(task_id):
    """Delete a task by ID"""
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        session.delete(task)
        session.commit()
        click.echo(Fore.CYAN + f"Deleted task {task_id}")
        click.echo(Style.RESET_ALL)
    else:
        click.echo(Fore.RED + f"Task with ID {task_id} does not exist.")
        click.echo(Style.RESET_ALL)


if __name__ == "__main__":
    taskly()
