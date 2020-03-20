""" -------------------------------------------------------PART 4--------------------------------------------------------- """
"""------------------------------------------------------------------------------------------------------------------------"""
# In the Northwind database, what is the type of relationship between the Employee and Territory tables?
"""
The relationship between employees and territories is many-to-many.
One employee can have many territories and one territory can have many employees.
As a result of this relationship, a joining table - EmployeeTerritory is used.
"""

# What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?
"""
Document stores have the advantages of greater scalability (higher performance) and greater flexibility.
These can be pros or cons depending on what is to be achieved. The greater scalability results in less readability.
It'll be harder to query and manage the data. The greater flexibilty also means it'll be less ACID-compliant.
(Atomicity, consistency, isolation, durability)
If the correctness of transactions is mission critical, then document stores are not a good choice.
"""

# What is "NewSQL", and what is it trying to achieve?
"""
NewSQL is a mixture between document stores like MongoDB and relational databases like PostgreSQL. It's an attempt
at getting the best of both worlds. The greater scalability and flexibility of document stores without the downsides
of less ACID compliance and less readability. One domain this could be useful is banking where ACID is very important, and 
more scalability is as well.
"""