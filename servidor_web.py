from flask import Flask, redirect, url_for, request
import pymysql.cursors
from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("templates/"))

app = Flask(__name__)

HEAD='<link rel= "stylesheet" type= "text/css" href= "static/main.css">'

@app.route('/',methods = ['GET'])
def home():
	#preparar un HTML bàsic
	HTML=""
	HTML+='<link rel= "stylesheet" type= "text/css" href= "static/main.css">'
	HTML+="<div style='display: flex;flex-direction: column;align-items: flex-start;'>"
	HTML+="<h1>Google trucho</h1>"
	
	HTML+="<form action='search' method='GET'>"
	HTML+="<input name='s'>"
	HTML+="<input type='submit'>"
	HTML+="</form>"

	if request.method == 'GET':
		search = request.args.get('search')
		
		if search is not None:
			HTML+="<h3>Resultats</h3>"
			HTML+='<div class="apps">'
			#afegim els resultats
			HTML+='Resultats per a '+search
			#aqui podem posar la conexió a la BD
			HTML+='</div>'

		return HTML

@app.route("/search",methods = ['GET'])
def loginProcess():

	connection = pymysql.connect(host='192.168.1.79',
							user='remoto',
							password='12345',
							database='steam',
							cursorclass=pymysql.cursors.DictCursor)
	
	cursor= connection.cursor()
	s = request.args.get('s')
	sql = 'SELECT * FROM steam.	apps WHERE name LIKE "%'+s+'%"'
	print(sql)
	#l'executem
	cursor.execute(sql)
	#atrapem els resultats, podem rebre tots o nomes un amb fetchone()
	resultats = cursor.fetchall()
	
	HTML=''
	for app in resultats:
		HTML+='<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/'+str(app["appid"])+'/header.jpg" style="border-radius:12px">'
		HTML+='<h3 class="titulo">'+app["name"]+'</h3>'


	#print("RESULTATS",resultats)
	
	return HTML

@app.route("/app/<int:appid>")
def app_detail(appid):
	print(appid)
    # La variable appid és un int
	#html_response = "<h1>La meva App ID: "+str(appid)+"</h1>"
	#return html_response
	template = environment.get_template("app.html")
	return template.render(appid=appid,anycreacio=1982)

if __name__ == '__main__':
	app.run(debug = True)

