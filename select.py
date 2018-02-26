# SELECT statement

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
"""
    # Use a for loop to iterate through the database, printing the results line by line

    for row in c.execute("SELECT firstname, lastname from employees"):
        print row # this shows it in unicode, and is not very pretty.
"""
# this method for prettier output
c.execute("SELECT firstname, lastname from employees")

# Fetchall() retrieves all records from the query
rows = c.fetchall()

# output the rows to the screen, row by row
for r in rows:
    print r[0], r[1]
