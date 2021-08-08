#!/usr/bin/python3
"""SQL query for lists all states from the database hbtn_0e_0_usa"""

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
    query_rows = cursor.fetchall()
    # print rows
    for row in query_rows:
        print(row)
    # disconnect from server
    cursor.close()
    db.close()
