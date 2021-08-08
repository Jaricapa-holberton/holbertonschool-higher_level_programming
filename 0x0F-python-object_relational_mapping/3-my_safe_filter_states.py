#!/usr/bin/python3
"""
Query for in arguments and display all values in the
states table of hbtn_0e_0_usa where name matches the
argument. But this time, write one that is safe from
MySQL injections.
"""

import MySQLdb
from sys import argv

# create a function for set a layer of security against the SQL injections


def main():
    """
    Executes a SQL query in MySQLdb
    """
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
    query = "SELECT * FROM states ORDER BY id ASC"
    # execute SQL query using execute() method.
    cursor.execute(query)
    # Fetch results as were displayed in the intranet example
    states = cursor.fetchall()
    # print rows
    for state in states:
        if state[1] == statename:
            print(state)
    # disconnect from server
    cursor.close()
    db.close()

# execute the function for security


if __name__ == "__main__":
    main()
