#!/usr/bin/python3
<<<<<<< HEAD
"""
Lists all states with a name starting with N
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * \
    FROM states \
    WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS \
    LIKE 'N%';")
    states = cur.fetchall()

    for state in states:
        print(state)
=======
import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) == 4:
        conn = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306,
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%';")
        rows = cur.fetchall()
        for row in rows:
            print(ow)
>>>>>>> 808d56eb8db81523fe67aa8fb34f2d374a178dfa
