CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY,
    name TEXT,
    associated_file_name TEXT,
    associated_file_data BLOB,
    version TEXT
);
