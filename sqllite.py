import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

table_info ="""
create table Student(Name varchar(25), class varchar(25),
Section varchar(25), Marks INT)
"""
cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('John','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Mukesh','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Jacob','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')

print("The inserted records are")

data = cursor.execute('''select * from Student''')
for row in data :
    print(row)

connection.commit()
connection.close()
