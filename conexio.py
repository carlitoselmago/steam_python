import pymysql.cursors

connection = pymysql.connect(host='192.168.1.79',
							user='web2',
							password='12345',
							database='steam',
							cursorclass=pymysql.cursors.DictCursor)

print(connection)

cursor= connection.cursor()

print(cursor)

sql = 'SELECT * FROM apps WHERE name LIKE "%War%"'
#l'executem
cursor.execute(sql)
#atrapem els resultats, podem rebre tots o nomes un amb fetchone()
resultats = cursor.fetchall()

for res in resultats:
    print(res["name"])