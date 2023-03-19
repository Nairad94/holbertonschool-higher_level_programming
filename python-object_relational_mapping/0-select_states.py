#!/usr/bin/python3
""" 0-select_states module"""
from sys import argv
import MySQLdb


def select_states():
    """ lists all states from the database hbtn_0e_0_usa"""
    database = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], database=argv[3])
    cur = database.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    select_states()
