#!/usr/bin/python3
"""SQL query for lists all states with a name starting with N (upper N)"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # get args from input
    user = argv[1]
    password = argv[2]
    dbname = argv[3]
    # Open database connection
    db = MySQLdb.connect(
         host="localhost",
         port=3306,
         user=user,
         passwd=password,
         db=dbname,
         charset="utf8")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # execute SQL query using execute() method.
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    # Fetch results as were displayed in the intranet example
    states = cursor.fetchall()
    # print rows
    for state in states:
        if (state[1][0] == 'N'):
            print(state)
    # disconnect from server
    cursor.close()
    db.close()
