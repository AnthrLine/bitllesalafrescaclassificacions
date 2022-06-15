from flask import Flask, render_template, send_file
import requests
import time
from modules import sheetoperator, mainhtmloperator, eqfsheetoperator
app = Flask('app')

@app.route('/')
def main():
  return render_template("index.html")
	
@app.route('/testeqf')
def testeqf():
	eqfsheetoperator.exec()
	return ("Que sigui el que déu vulgui")

@app.route('/equipsfederats')
def equipsfederats():
	return render_template('eqf.html')

@app.route('/equipsnofederats')
def equipsnofederats():
	return("Equips no federats")

@app.route('/individualnofederats')
def individualnofederats():
	return("Individual no federats")

@app.route('/individualfederats')
def individualfederats():
	return("Individual federats")

@app.route('/individual20102014')
def individual20102014():
	return("Individual 2010 2014")

@app.route('/individual20062009')
def individual20062009():
	return("Individual 2006 2009")

@app.route('/execsheetoperator')
def execsheetoperator():
	sheetoperator.exec()
	mainhtmloperator.exec()
	eqfsheetoperator.exec()
		
	return('Que sigui el que déu vulgui :)')

if __name__ == '__main__':
	app.config['TESTING'] = True
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(host='0.0.0.0', port=8080)
