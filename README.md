# Todo CLI

## Description

A small command-line to-do list application written in Python.  
It lets you add, list, and delete tasks from the terminal, and saves 
them in a plain text file so they persist between runs.

## Features

- Add a task
- List all tasks (numbered)
- Delete a task by its number

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/behboodi-dev/todo-cli.git
cd todo

# 2. Create a virtual environment
python -m venv .venv

# 3. Activate it
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# macOS / Linux:
source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create your environment file
cp .env.example .env
# On Windows: copy .env.example .env

# Add a task
python todo.py add "study python"

# List all tasks
python todo.py list

# Delete a task
python todo.py delete 1
