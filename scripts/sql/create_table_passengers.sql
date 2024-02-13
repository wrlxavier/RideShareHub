CREATE TABLE IF NOT EXISTS passengers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at DATETIME NOT NULL DEFAULT (datetime('now')),
    edited_at DATETIME,
    deleted_at DATETIME,
    passenger_name TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    whatsapp_link TEXT NOT NULL
);