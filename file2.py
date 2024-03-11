To extend the code provided so it prints all retrieved records from the table students, instead of just one record, you can use a loop to iterate through the results of the execute method.

  The fetchone() method retrieves a single row from the query result set. If you wish to retrieve and print all rows, fetchall() is more appropriate. Alternatively, you can iterate directly
over the resultset as it is an iterable object.

Here is how you can modify the code to print each record in the students table:

import sqlite3

# Connect to the SQLite database
con = sqlite3.connect('ces.db')
cur = con.cursor()

# Execute the query to select all records from the students table
resultset = cur.execute("select * from students")

# Fetch all records from the resultset
all_records = resultset.fetchall()

# Iterate over each record and print it
for record in all_records:
    print(record)
Or, using direct iteration over the resultset for more efficient memory usage:

python


Explain
import sqlite3

# Connect to the SQLite database
con = sqlite3.connect('ces.db')
cur = con.cursor()

# Execute the query to select all records from the students table
resultset = cur.execute("select * from students")

# Directly iterate over the resultset and print each record
for record in resultset:
    print(record)

# Close the connection when done
con.close()
Both methods will print each row of the students table to the console. The first method retrieves all rows at once and stores them in a list (all_records), which is then iterated over to print each record. The second method iterates over the resultset without storing all rows in memory at once, making it more efficient for large datasets. Make sure to close the database connection when you're done to release resources.
