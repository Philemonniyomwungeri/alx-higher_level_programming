#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    # Create a cursor object
    cur = conn.cursor()

    # Execute the query to select all states
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows and display them
    for row in cur.fetchall():
        print(row)

    # Close cursor and connection
    cur.close()
    conn.close()
