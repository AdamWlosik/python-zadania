import sqlite3
from datetime import datetime


class Database:
    def __init__(self, path):
        self.connect = sqlite3.connect(path)

    def create_table(self, tabel_name):
        qurey = (
            f"CREATE TABLE IF NOT EXISTS {tabel_name}(id INTEGER PRIMARY KEY,"
            f" name TEXT UNIQUE, note TEXT, create_time DATETIME);"
        )
        self.connect.execute(qurey)

    def add_note(self, name, note, tabel_name):
        create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = f"INSERT INTO {tabel_name} (name, note, create_time) VALUES (?, ?, ?)"
        self.connect.execute(query, (name, note, create_time))

    def remove_note(self, name, tabel_name):
        query = f"DELETE FROM {tabel_name} WHERE name = ?"
        self.connect.execute(query, (name,))

    def display_notes(self, tabel_name):
        query = f"SELECT * FROM {tabel_name}"
        print(self.connect.execute(query).fetchall())

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if isinstance(exc_val, Exception):
            self.connect.rollback()
        else:
            self.connect.commit()
        self.connect.close()


with Database("notebook.db.sqlite3") as database:
    database.create_table("Notes")
    database.add_note("Note 1", "Note 1 text", "Notes")
    database.display_notes("Notes")
    database.add_note("Note 2", "Note 2 text", "Notes")
    database.display_notes("Notes")
    database.remove_note("Note 2", "Notes")
    database.display_notes("Notes")
