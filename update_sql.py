import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("UPDATE inventory SET Quantity = 4 WHERE Model='Galaxy'")
    c.execute("UPDATE inventory SET Quantity = 3 WHERE Model='Jazz'")

    print "\nNEW DATA:\n"

    c.execute("SELECT * FROM inventory WHERE Make='Ford'") # Selects all the records where the make is Ford, if it just
    # said 'SELECT * FROM inventory' it would just select everything


    rows = c.fetchall()

    for r in rows:
        print r[0], r[1], r[2]
