import mysql.connector;

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234",
  database='banking'
)
print(db_connection)

cursor = db_connection.cursor()
sql = '''SELECT * from customer'''
cursor.execute(sql)
result = cursor.fetchmany(size =2);
print(result)
