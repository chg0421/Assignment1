# https://www.tutorialspoint.com/sqlite/sqlite_python.htm


import sqlite3

try:
    connection = sqlite3.connect("company.db")
except Exception as e:
    print(e)
else:
    print("Opened database successfully")
finally:
    print("Finishing connecting to database")

cursor = connection.cursor()

# delete
cursor.execute("""DROP TABLE employee;""")

sql_command = """
CREATE TABLE employee (
emp_id INTEGER PRIMARY KEY,
gender VARCHAR(1),
age INTEGER(2),
sales INTEGER (3),
bmi VARCHAR (11),
salary INTEGER,
birth_date DATE);"""

cursor.execute(sql_command)

# sql_command = """INSERT INTO employee (emp_id, gender, age, sales, bmi,salary,birth_date)
#     VALUES (NULL, "F", 23, 300, "Normal", 45000, "1990-10-25");"""
# cursor.execute(sql_command)


employee_data = [("A001", "F", 23, 300, "Normal", 35000, "1989-08-05"),
              ("A001", "M", 25, 600, "Obesity", 55000, "1999-07-05")]

for p in employee_data:
    format_str = """INSERT INTO employee (emp_id, gender, age, sales, bmi,salary,birth_date)
    VALUES (NULL, "{gender}", "{age}", "{sales}", "{bmi}", "{salary}", "{birth_date}");"""

    sql_command = format_str.format(emp_id=p[0], gender=p[1], age=p[2], sales = p[3], bmi = p[4],salary = p[5],birth_date = p[6])
    cursor.execute(sql_command)

# never forget this, if you want the changes to be saved:
connection.commit()


cursor.execute("SELECT * FROM employee")
print("fetchall:")
result = cursor.fetchall()
for r in result:
    print(r)
cursor.execute("SELECT * FROM employee")
print("\nfetch one:")
res = cursor.fetchone()
print(res)


connection.close()