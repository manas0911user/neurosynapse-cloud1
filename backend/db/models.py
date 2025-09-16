import sqlite3
import os

DB_PATH = "logs/functions.db"

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS executions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        latency REAL,
        success BOOLEAN,
        cpu REAL,
        memory REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

def save_execution(result: dict):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO executions (latency, success, cpu, memory)
    VALUES (?, ?, ?, ?)
    """, (
        result.get("latency"),
        1 if result.get("success") else 0,
        result.get("cpu"),
        result.get("memory"),
    ))

    conn.commit()
    conn.close()
