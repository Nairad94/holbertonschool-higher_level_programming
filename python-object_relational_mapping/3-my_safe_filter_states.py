#!/usr/bin/python3
"""filter states module"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    database = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], database=argv[3])
    cur = database.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", (argv[4],))
    [print(row) for row in cur.fetchall()]
