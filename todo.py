"""A simple command-line to-do list application."""

import os
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


