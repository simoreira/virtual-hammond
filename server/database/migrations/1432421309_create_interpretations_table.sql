CREATE TABLE interpretations(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    song_id INTEGER,
    registry TEXT,
    effects TEXT,
    wave_file TEXT UNIQUE,
    votes INTEGER DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
