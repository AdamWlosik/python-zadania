import sqlite3


class Database:

    def __init__(self, path):
        self.con = sqlite3.connect(path)

    def create_table(self):
        query = (
            "CREATE TABLE IF NOT EXISTS Customers(id INTEGER PRIMARY KEY, name TEXT NOT NULL, surname TEXT NOT NULL, "
            "data_joined DATE NOT NULL);"
        )

        self.con.execute(query)

    def add_to_customers(self, name, surname, data_joined):
        query = "INSERT INTO Customers (name, surname, data_joined) VALUES (?, ?, ?)"
        self.con.execute(query, (name, surname, data_joined))

    def preview_table(self, table_name):
        query = f"SELECT * FROM {table_name}"
        results = self.con.execute(query).fetchall()
        print(results)

    def delete_based_on_id(self, table_name, id):
        query = f"DELETE FROM {table_name} WHERE id = {id}"
        self.con.execute(query)

    def update_name_based_on_id(self, table_name, id, name):
        query = f"UPDATE {table_name} SET name = ? WHERE id = {id}"
        self.con.execute(query, (name,))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        if isinstance(exc_val, Exception):
            self.con.rollback()
        else:
            self.con.commit()
        self.con.close()


with Database("example-database.sqlite3") as db:
    db.create_table()
    db.add_to_customers("John", "Wick", "2000-09-02")
    db.preview_table("Customers")
    # db.add_to_customers('James', 'Bond', '2002-05-16')
    db.delete_based_on_id("Customers", "4")
    db.preview_table("Customers")
    db.update_name_based_on_id("Customers", "3", "Grzegorz")
    db.preview_table("Customers")
