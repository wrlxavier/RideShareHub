CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at DATETIME NOT NULL DEFAULT (datetime('now')),
    edited_at DATETIME,
    deleted_at DATETIME,
    ticket_status_id INTEGER NOT NULL,
    scheduled_date DATETIME NOT NULL,
    journey_id INTEGER NOT NULL,
    passenger_id INTEGER NOT NULL,
    ticket_price REAL NOT NULL,
    FOREIGN KEY (ticket_status_id) REFERENCES ticket_status(id),
    FOREIGN KEY (journey_id) REFERENCES journey(id),
    FOREIGN KEY (passenger_id) REFERENCES passengers(id)
);