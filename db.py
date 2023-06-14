import mysql.connector

# Establish a connection to the database
cnx = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='your_database'
)

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()

# Create a table
create_table_query = '''
    CREATE TABLE employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        salary FLOAT
    )
'''
cursor.execute(create_table_query)
print("Table created successfully.")

# Insert a new record
insert_query = '''
    INSERT INTO employees (name, age, salary)
    VALUES (%s, %s, %s)
'''
record_data = ('John Doe', 30, 5000.0)
cursor.execute(insert_query, record_data)
cnx.commit()
print("Record inserted successfully.")

# Read records from the table
select_query = '''
    SELECT id, name, age, salary
    FROM employees
'''
cursor.execute(select_query)
records = cursor.fetchall()
print("Records:")
for record in records:
    print(record)

# Update a record
update_query = '''
    UPDATE employees
    SET salary = %s
    WHERE id = %s
'''
update_data = (6000.0, 1)
cursor.execute(update_query, update_data)
cnx.commit()
print("Record updated successfully.")

# Delete a record
delete_query = '''
    DELETE FROM employees
    WHERE id = %s
'''
delete_data = (1,)
cursor.execute(delete_query, delete_data)
cnx.commit()
print("Record deleted successfully.")

# Close the cursor and connection
cursor.close()
cnx.close()
