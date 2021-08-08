#!/usr/bin/python3
"""
Query for takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name
matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # get args from input
    user = argv[1]
    password = argv[2]
    dbname = argv[3]
    statename = argv[4]
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
    # set the query statement
    query = "SELECT * FROM states \
                WHERE BINARY `name` = '{}' \
                ORDER BY id ASC".format(statename)
    # execute SQL query using execute() method.
    cursor.execute(query)
    # Fetch results as were displayed in the intranet example
    states = cursor.fetchall()
    # print rows
    for state in states:
        print(state)
    # disconnect from server
    cursor.close()
    db.close()
