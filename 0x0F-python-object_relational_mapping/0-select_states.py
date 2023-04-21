#!/usr/bin/python3
<<<<<<< HEAD
"""
Lists all states from the database hbtn_0e_0_usa
"""
=======
""" Listsa all the states from the database"""
import MySQLdb
>>>>>>> 808d56eb8db81523fe67aa8fb34f2d374a178dfa
import sys
import MySQLdb

if __name__ == '__main__':
<<<<<<< HEAD
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states;")
    states = cur.fetchall()

    for state in states:
        print(state)
=======
    if len(sys.argv) == 4:
        conn = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306,
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM states;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
>>>>>>> 808d56eb8db81523fe67aa8fb34f2d374a178dfa
