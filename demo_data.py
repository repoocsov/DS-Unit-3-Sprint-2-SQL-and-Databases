# demo_data.py
import sqlite3
import os

""" PART 1 """
DB_FILEPATH = os.path.join(os.path.dirname(__file__), 'demo_data.sqlite3')

# Connect to DB
conn = sqlite3.connect(DB_FILEPATH)
curs = conn.cursor()


# Create table
query = """
CREATE TABLE IF NOT EXISTS demo (
  s varchar(1) NOT NULL,
  x Integer NOT NULL,
  y Integer NOT NULL);
"""
result = curs.execute(query).fetchall()

# Insert data
# NOTE: you are going to want to delete an entries already in the DB otherwise these values will duplicate
insertion_query = "INSERT INTO demo (s, x, y) VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7)"
result = curs.execute(insertion_query).fetchall()
conn.commit()
print("PART 1 BUSINESS QUESTIONS")

# Number of rows
sql = """
SELECT
	COUNT(*) AS "Number of Rows"
FROM demo
"""
result = curs.execute(sql).fetchall()
print('ROWS:', result)

# How many rows are there where both x and y are at least 5?
sql = """
SELECT
	COUNT(*) AS "Rows"
FROM demo
WHERE x >= 5
AND y >= 5
"""
result = curs.execute(sql).fetchall()
print('ROWS (X >=5 and y >= 5):', result)

# How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)?
sql = """
SELECT
	COUNT(DISTINCT y) AS "Unique y values"
FROM demo
"""
result = curs.execute(sql).fetchall()
print('ROWS WITH UNIQUE Y:', result)

# Close connection
curs.close()
