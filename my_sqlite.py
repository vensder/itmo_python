
import sqlite3

#открываем или создаем бд
conn = sqlite3.connect('example.db')

# создаем курсор - точка доступа к таблице БД
c = conn.cursor()


# Create table 
try:
	c.execute('''CREATE TABLE students (id INTEGEr, name text, date text)''')
	# Save (commit) the changes
	conn.commit()
	
	print('create students...')

except sqlite3.OperationalError:
	pass
	

# Create table 
try:
	c.execute('''CREATE TABLE books (id INTEGER, name text, date text)''')
	# Save (commit) the changes
	conn.commit()
	
	print('create books...')

except sqlite3.OperationalError:
	pass
	
# get data from tables
c.execute('SELECT * FROM students')
# берем первую запись
print(c.fetchone())

# количество записей
print('rowcount: ', c.rowcount, 'descr: ', c.description)
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.

# Insert a row of data
c.execute("INSERT INTO students VALUES ('0','Ivan','1980-01-05')")
c.execute("INSERT INTO students VALUES ('1','Mariya','1985-03-05')")

conn.commit()

for  row in c.execute("SELECT * FROM students"):
	print(row)


# get data about students
c.execute('SELECT * FROM students')
print(c.fetchone())

conn.close()

