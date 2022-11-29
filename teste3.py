import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="veiculos"
)

mycursor = mydb.cursor()
deletar = input('Qual você quer apagar?' )
sql = "DELETE FROM tipos WHERE id = %s"
val = (deletar,)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")