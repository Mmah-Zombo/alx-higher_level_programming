#!/usr/bin/python3
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
