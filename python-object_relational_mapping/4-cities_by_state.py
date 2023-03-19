#!/usr/bin/python3
"""my filter states module"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    database = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], database=argv[3])
    cur = database.cursor()
    cur.execute("SELECT ROW_NUMBER() OVER(), \
                cities.name,states.name \
                FROM cities, states \
                WHERE state_id = states.id")
    [print(row) for row in cur.fetchall()]
    