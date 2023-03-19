#!/usr/bin/python3
"""filter states module"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    databade = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], database=argv[3])
    cur = databade.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    [print(row) for row in cur.fetchall() if row[1][0] == 'N']
