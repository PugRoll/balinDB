import sqlite3
import os

#open the database
conn = sqlite3.connect('d.db')
cursor = conn.cursor()


#Read the .tar.gz file as binary_data
with open('balinAdd.tar.gz', 'rb') as file:
    file_data = file.read()


cursor.execute("INSERT INTO data (name, associated_file_name, associated_file_data, version) VALUES (?, ?, ?, ?)",
               ('balinAdd', 'balinAdd.tar.gz', file_data, '1.0'))

with open('balinSubtract.tar.gz', 'rb') as file:
    file_data = file.read()

cursor.execute("INSERT INTO data (name, associated_file_name, associated_file_data, version) VALUES (?, ?, ?, ?)",
               ('balinSubtract', 'balinSubtract.tar.gz', file_data, '1.0'))
conn.commit()
conn.close()
