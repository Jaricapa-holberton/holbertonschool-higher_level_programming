#!/usr/bin/python3
"""
Query for lists all cities from the database hbtn_0e_4_usa.
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
    # statename = argv[4]
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
    query = "SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`"
    # execute SQL query using execute() method.
    cursor.execute(query)
    # Fetch results as were displayed in the intranet example
    cities = cursor.fetchall()
    # print rows
    for city in cities:
        print(city)
    # disconnect from server
    cursor.close()
    db.close()

# execute the function for security


if __name__ == "__main__":
    main()
