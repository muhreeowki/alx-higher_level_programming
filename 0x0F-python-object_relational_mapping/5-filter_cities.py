#!/usr/bin/python3
"""
takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where
name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    state_name = sys.argv[4]
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
    )
    cur = db.cursor()
    cur.execute(
        """
    SELECT cities.name
    FROM cities JOIN states
    ON states.id = cities.state_id
    WHERE states.name=%s
    ORDER BY cities.id
    """,
        (state_name,),
    )
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    db.close()
