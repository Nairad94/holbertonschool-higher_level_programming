#!/usr/bin/python3
"""filter cities module"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    database = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], database=argv[3])
    cur = database.cursor()
    cur.execute("SELECT * \
                FROM cities AS c \
                INNER JOIN states AS s \
                ON c.state_id = s.id")
    print(', '.join([row[2] for row in cur.fetchall() if row[4] == argv[4]]))
