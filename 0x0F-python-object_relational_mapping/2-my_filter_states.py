#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Validate the number of arguments
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Establish a connection to the database
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )

        # Create a cursor object
        cur = conn.cursor()

        # Execute the SQL query with user input as a parameter
        cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", (state_name,))

        # Fetch all rows from the result set
        rows = cur.fetchall()

        # Print each row
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close cursor and connection
        if cur:
            cur.close()
        if conn:
            conn.close()

