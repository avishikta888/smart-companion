from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import time

app = FastAPI()

# Database setup
conn = sqlite3.connect("data.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT,
    created_at TEXT
)
""")
conn.commit()

class TaskInput(BaseModel):
    task: str

@app.post("/break-task")
def break_task(data: TaskInput):
    task = data.task

    # Save task (privacy-first local storage)
    cursor.execute(
        "INSERT INTO tasks (task, created_at) VALUES (?, ?)",
        (task, time.strftime("%Y-%m-%d %H:%M:%S"))
    )
    conn.commit()

    # SIMPLE AI LOGIC (Micro-Wins)
    steps = [
        f"Take a deep breath and prepare to start: {task}",
        "Clear your workspace (1 minute)",
        "Start the first tiny part only (2 minutes)",
        "Take a short break and acknowledge progress"
    ]

    return {
        "original_task": task,
        "micro_steps": steps
    }
