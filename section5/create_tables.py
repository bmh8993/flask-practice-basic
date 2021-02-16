import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
# if you want to use auto increament, don't use int, use the whole word INTEGER
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
# real is a number with a decimal point, such as 10.99 for example.
# cursor.execute("INSERT INTO items VALUES ('test', 10.99)")
cursor.execute(create_table)

connection.commit()

connection.close()
