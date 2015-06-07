CREATE TABLE interpretations(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    song_id INTEGER,
    registry TEXT,
    effects TEXT,
    wave_file TEXT,
    votes INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
