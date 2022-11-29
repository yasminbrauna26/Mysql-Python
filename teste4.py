import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="veiculos"
)

mycursor = mydb.cursor()
nome = input('Qual você quer mudar?' )
id = input('Qual id você quer alterar?')
sql = "UPDATE tipos SET nome = %s where id = %s"
val = (nome, id)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")