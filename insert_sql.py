import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    data = [('Ford', 'Focus', 8),
            ('Ford', 'Galaxy', 3),
            ('Ford', 'Mondeo', 17),
            ('Honda', 'Civic', 9),
            ('Honda', 'Jazz', 1)]

    c.executemany('INSERT INTO inventory VALUES(?, ?, ?)', data)
    