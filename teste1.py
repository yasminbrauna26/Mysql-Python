import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="veiculos"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM tipos")

tipos = mycursor.fetchall()

for id, nome in tipos:
  print(id, nome)

