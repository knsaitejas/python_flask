from flask import Flask, render_template, request, redirect, session, url_for
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	session['activity'] = ''
	session['score'] = 0
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
	output = ''
	if request.form['building'] == 'farm':
		session['farm'] = int(random.randrange(10,21))
		session['score'] += session['farm']
		output = 'Earned '+str(session['farm'])+' from farm!'
	elif request.form['building'] == 'cave':
		session['cave'] = int(random.randrange(5,11))
		session['score'] += session['cave']
		output = 'Earned '+str(session['cave'])+' from cave!'
	elif request.form['building'] == 'house':
		session['house'] = int(random.randrange(2,6))
		session['score'] += session['house']
		output = 'Earned '+str(session['house'])+' from house!'
	session['activity'] += "<p class='win'>"+output+"</p>"
	if request.form['building'] == 'casino':
		session['casino'] = int(random.randrange(-50,51))
		session['score'] += session['casino']
		if session['casino'] < 0:
			output = 'Entered a casino and lost '+str(session['casino'])+'...Ouch..'
			session['activity'] += "<p class='loss'>"+output+'</p>'
		else:
			output = 'Entered a casino and WON '+str(session['casino'])+'...Woohoo!!'
			session['activity'] += "<p class='win'>"+output+'</p>'

	return render_template('index.html',activity=session['activity'], score=session['score'])
	

app.run(debug=True)