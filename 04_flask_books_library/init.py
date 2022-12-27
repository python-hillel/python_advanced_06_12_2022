import sqlite3
from faker import Faker

conn = sqlite3.connect('book.db')

with open('schema.sql', 'rt', encoding='utf-8') as file:
    conn.executescript(file.read())

cursor = conn.cursor()

f = Faker()
for _ in range(25):
    title = f.word().capitalize()
    author = f'{f.first_name()} {f.last_name()}'
    cursor.execute('INSERT INTO book(title, author) VALUES (?, ?)', (title, author))

conn.commit()
cursor.close()
conn.close()

