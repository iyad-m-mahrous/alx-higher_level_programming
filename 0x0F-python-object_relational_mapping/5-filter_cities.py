#!/usr/bin/python3
""" 5. All cities by states """
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
    cur.execute("SELECT c.name FROM cities as c\
                INNER JOIN states as s ON s.id = c.state_id\
                WHERE s.name = %s\
                ORDER BY c.id", (sys.argv[4],))
    query_rows = cur.fetchall()
    print(', '.join([city for row in query_rows for city in row]))
    cur.close()
    db.close()
