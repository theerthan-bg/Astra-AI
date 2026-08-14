CREATE TABLE tasks (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT NOT NULL,

    completed INTEGER DEFAULT 0,

    created_at TEXT NOT NULL

);


CREATE TABLE conversations (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_message TEXT NOT NULL,

    ai_response TEXT NOT NULL,

    created_at TEXT NOT NULL

);