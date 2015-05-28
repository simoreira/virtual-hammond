CREATE TABLE interpretations(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    song_id INTEGER,
    registration TEXT,
    effects TEXT,
    wave_file TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
