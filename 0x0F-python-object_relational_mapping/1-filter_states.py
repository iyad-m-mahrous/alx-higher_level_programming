#!/usr/bin/python3
""" 0. Get all states """
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
    try:
        cur.execute("SELECT * FROM `states` WHERE name LIKE 'N%' ORDER BY `id`")
        query_rows = cur.fetchall()
    except Exception as e:
        pass
    else:
        [print(row) for row in query_rows]
    cur.close()
    db.close()
