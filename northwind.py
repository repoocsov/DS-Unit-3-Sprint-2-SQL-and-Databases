# northwind.py
import sqlite3
import os

# Connect to DB
DB_FILEPATH = os.path.join(os.path.dirname(__file__), 'northwind_small.sqlite3')
conn = sqlite3.connect(DB_FILEPATH)
curs = conn.cursor()

# What are the ten most expensive items (per unit price) in the database?
print("PART 2 BUSINESS QUESTIONS")
sql = """
SELECT
	ProductName,
	UnitPrice AS "Price"
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
"""
result = curs.execute(sql).fetchall()
print('\nTOP 10 MOST EXPENSIVE ITEMS:', result)

# What is the average age of an employee at the time of their hiring?
sql = """
SELECT
	AVG(julianday(HireDate) - julianday(BirthDate)) / 365 AS "Average hire age"
FROM Employee
"""
result = curs.execute(sql).fetchall()
print('\nAVERAGE HIRE DATE AGE:', result)

# How does the average age of employee at hire vary by city?
sql = """
SELECT
	City,
	AVG(julianday(HireDate) - julianday(BirthDate)) / 365 AS "Average hire age"
FROM Employee
GROUP BY City
"""
result = curs.execute(sql).fetchall()
print('\nAVERAGE HIRE DATE AGE PER CITY:', result)


""" PART 3 """
# What are the ten most expensive items (per unit price) in the database and their suppliers?
sql = """
SELECT
	CompanyName,
	ProductName,
	UnitPrice AS "Price"
FROM Product
JOIN Supplier
ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10
"""
result = curs.execute(sql).fetchall()
print('\nTOP 10 MOST EXPENSIVE ITEMS AND SUPPLIERS:', result)

# What is the largest category (by number of unique products in it)?
sql = """
SELECT
	CategoryName,
	COUNT(CategoryName) AS "Products"
FROM Product
JOIN Category
ON Product.CategoryId = Category.Id
GROUP BY CategoryName
ORDER BY Products DESC
LIMIT 1
"""
result = curs.execute(sql).fetchall()
print('\nLARGEST CATEGORY:', result)

## Who's the employee with the most territories?
sql = """
SELECT
	LastName,
	FirstName,
	COUNT(EmployeeId) AS "Territories"
FROM Employee
JOIN EmployeeTerritory
ON Employee.Id = EmployeeTerritory.EmployeeId
GROUP BY EmployeeId
ORDER BY Territories DESC
LIMIT 1
"""
result = curs.execute(sql).fetchall()
print('\nEMPLOYEE WITH MOST TERRITORIES:', result)


# Close the connection
curs.close()