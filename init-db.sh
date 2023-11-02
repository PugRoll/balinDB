#!/bin/sh

#create database
sqlite3 /app/d.db

#Create a table to store the data
sqlite3 /app/d.db <<EOF
CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY,
    name TEXT,
    associated_file_name TEXT,
    associated_file_data BLOB,
    version TEXT
);
EOF

echo ".exit"

#Execute python script to insert data into database
python /app/convertToBlob.py


