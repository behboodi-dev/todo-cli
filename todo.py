"""A simple command-line to-do list application."""

import os
import argparse
from dotenv import load_dotenv

load_dotenv()

TASKS_FILE=os.getenv("TASKS_FILE","tasks.txt")

def load_tasks():

    """Read tasks from the file. Return an empty list if the file doesn't exist."""

    try:
        with open(TASKS_FILE,"r",encoding="utf-8") as f:
            tasks=[]
            for line in f:
                tasks.append(line.rstrip('\n'))
        return tasks
    except FileNotFoundError:
        return[]

def save_tasks(tasks):

    """Write tasks to the file, one per line."""

    with open(TASKS_FILE,'w',encoding='utf-8')as f:
        for task in tasks:
             f.write(f"{task}\n")

def add_task(task):

    """Add a new task to the list and save it."""

    tasks=load_tasks()
    tasks.append(task)
    save_tasks(tasks)   

def list_tasks():

    """Print all tasks, numbered starting from 1."""

    tasks=load_tasks()

    if not tasks:
        print('tasks not found.')

    i = 1
    for task in tasks:
        print(f"{i}. {task}")
        i += 1    


def main():

    """Parse command-line arguments and dispatch to the right function."""

    parser=argparse.ArgumentParser(description='A simple command-line To-Do app')

    subparsers=parser.add_subparsers(dest='command')

    add_parser=subparsers.add_parser('add')

    add_parser.add_argument('task',help="The task description")

    subparsers.add_parser('list',help="List all tasks")

    args=parser.parse_args()

    if args.command =='add':
        add_task(args.task)
        print(f'task added:{args.task}')
    elif args.command =='list':
        list_tasks()    

