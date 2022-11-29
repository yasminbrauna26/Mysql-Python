import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="veiculos"
)

mycursor = mydb.cursor()
sql = "select * from modelos m join tipos t on m.id_tipo=t.id"
mycursor.execute(sql)

linhas = mycursor.fetchall()

print(f'{"id":5} id_tipo id_marca nome_modelo id_veiculo nome_tipo')
for id, id_tipo, id_marca, nome_modelo, id_veiculo, nome_tipo in linhas:
  print(id, id_tipo, id_marca, nome_modelo, id_veiculo, nome_tipo)