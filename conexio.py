import pymysql.cursors

connection = pymysql.connect(host='192.168.1.158',
							user='remoto',
							password='12345',
							database='steam',
							cursorclass=pymysql.cursors.DictCursor)

print(connection)

cursor= connection.cursor()

sql = 'SELECT * FROM apps WHERE name LIKE "%war%"'
#l'executem
cursor.execute(sql)
#atrapem els resultats, podem rebre tots o nomes un amb fetchone()
resultats = cursor.fetchall()

for res in resultats:
    #print(res)
	gamename=res["name"]
	print("El meu game es diu ",gamename)
    #print(res["name"]," - " res["appid"])