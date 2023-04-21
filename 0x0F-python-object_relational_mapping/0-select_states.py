#!/usr/bin/env python3
import pymysql
import sys

if __name__ == '__main__':
    if len(sys.argv) == 4:
        conn = pymysql.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
            port=3306,
            )
        cur = conn.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        conn.close()
    else:
        print("Usage: ./list_states.py <mysql_username> <mysql_password> <database_name>")

