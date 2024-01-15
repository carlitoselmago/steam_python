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
	HTML+="<form>"
	HTML+="<input name='search'>"
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

