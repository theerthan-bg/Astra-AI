import sqlite3
from datetime import datetime


DATABASE = "astra.db"


def connection():

    db = sqlite3.connect(
        DATABASE
    )

    db.row_factory = sqlite3.Row

    return db


def initialize():

    db = connection()

    cursor = db.cursor()


    cursor.execute("""

        CREATE TABLE IF NOT EXISTS tasks (

            id INTEGER PRIMARY KEY
            AUTOINCREMENT,

            title TEXT NOT NULL,

            completed INTEGER DEFAULT 0,

            created_at TEXT

        )

    """)


    cursor.execute("""

        CREATE TABLE IF NOT EXISTS
        conversations (

            id INTEGER PRIMARY KEY
            AUTOINCREMENT,

            user_message TEXT,

            ai_response TEXT,

            created_at TEXT

        )

    """)


    db.commit()

    db.close()


def save_conversation(
    user_message,
    ai_response
):

    db = connection()

    db.execute("""

        INSERT INTO conversations
        (
            user_message,
            ai_response,
            created_at
        )

        VALUES (?, ?, ?)

    """, (

        user_message,

        ai_response,

        datetime.now().isoformat()

    ))


    db.commit()

    db.close()


def create_task(title):

    db = connection()

    cursor = db.cursor()


    cursor.execute("""

        INSERT INTO tasks
        (
            title,
            created_at
        )

        VALUES (?, ?)

    """, (

        title,

        datetime.now().isoformat()

    ))


    db.commit()

    task_id = cursor.lastrowid

    db.close()


    return task_id


def get_tasks():

    db = connection()

    cursor = db.cursor()


    cursor.execute("""

        SELECT *
        FROM tasks
        ORDER BY id DESC

    """)


    rows = cursor.fetchall()

    db.close()


    return [
        dict(row)
        for row in rows
    ]