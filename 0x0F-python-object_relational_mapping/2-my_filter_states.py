#!/usr/bin/python3
""" 2. Filter states by user input """
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` WHERE BINARY name = '{}'\
                ORDER BY id".format(sys.argv[4]))
    query_rows = cur.fetchall()
    [print(row) for row in query_rows]
    cur.close()
    db.close()
