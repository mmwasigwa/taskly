# Taskly -  CLI Project with SQL Database

## Introduction

- This Command Line Interface (CLI) project allows you to manage tasks using an SQL database as the backend storage. 
- Easily create, update, delete, and list tasks with this handy CLI tool.

## Features

- Create, update, and delete tasks.
- Set timer and stop timer for tasks
- Data using an SQL database.

## Prerequisites

Before using this CLI tool, ensure you have:
- virtual environment set up (Recommended)
- 
- nenessary dependencies install
- SQLite or your preferred SQL database

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/task-cli.git

Certainly! Here's a simplified Markdown format for your Task CLI project with an SQL database:

markdown
Copy code
# Task CLI Project with SQL Database

![CLI Project Logo](cli-project-logo.png)

## Introduction

This Command Line Interface (CLI) project allows you to manage tasks using an SQL database as the backend storage. Easily create, update, delete, and list tasks with this handy CLI tool.

## Features

- Create, update, and delete tasks.
- List tasks by status (completed or pending).
- Data persistence using an SQL database.

## Prerequisites

Before using this CLI tool, ensure you have:

- Node.js (v14+)
- npm (Node Package Manager)
- SQLite or your preferred SQL database

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/task-cli.git
Change to the project directory:

bash
Copy code
cd task-cli
Install dependencies:

bash
Copy code
npm install
Usage
Database Setup: Configure the SQL database (SQLite or other) as described in Database Setup.

Run the CLI:

bash
Copy code
npm start
Commands:

add: Create a new task.
update: Modify or mark a task as complete.
delete: Remove a task by its ID.
list: View tasks, optionally filtered by status.
exit: Close the CLI tool.
Database Setup
Database Configuration: Configure the database settings in config.js, specifying the database type and connection details.

Initialize Database:

bash
Copy code
npm run db:init
Database Connection: The CLI tool connects to the configured database automatically.

Contributing
Contributions are welcome. Report issues or submit pull requests on GitHub.

License
This project is licensed under the MIT License. See LICENSE for details.

