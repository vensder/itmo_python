import sqlite3


class ExamlpeConnect:
	
	def __init__(self):
		#открываем или создаем бд
		self.__conn = sqlite3.connect('example.db')

		# создаем курсор - точка доступа к таблице БД
		self.__conn = conn.cursor()

	def __del__(self):
		#destructor
		
		print('закрываем соединение')
		self.__conn.close()
	q
	def create
		# Create table 
		self.__create_table('books')
		self.__create_table('students')

		# Insert a row of data
		c.execute("INSERT INTO students VALUES ('0','Ivan','1980-01-05')")
		c.execute("INSERT INTO students VALUES ('1','Mariya','1985-03-05')")
		
	def __create_table(self, table_name):
		# Create table 
		try:
			self.__cursor.execute('CREATE TABLE {} (id INTEGER, name text, date text)'.format(table_name))
			# Save (commit) the changes
			self.__conn.commit()
			
			print('create {}...'.format(table_name))

		except sqlite3.OperationalError:
			pass
