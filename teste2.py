import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="veiculos"
)

mycursor = mydb.cursor()

tipo = input('Qual o tipo do veiculo?' )
sql = "INSERT INTO tipos (nome) VALUES (%s)"
val = (tipo,)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")