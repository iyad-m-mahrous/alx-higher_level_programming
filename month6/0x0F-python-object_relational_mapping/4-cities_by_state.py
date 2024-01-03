#!/usr/bin/python3
""" 4. Cities by states """
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
    cur.execute("SELECT c.id, c.name, s.name FROM cities as c\
                INNER JOIN states as s ON s.id = c.state_id\
                ORDER BY c.id")
    query_rows = cur.fetchall()
    [print(row) for row in query_rows]
    cur.close()
    db.close()
