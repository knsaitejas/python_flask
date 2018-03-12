from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	session['number'] = int(random.randrange(0, 101))
	return render_template('index.html',number=session['number'])

@app.route('/submit', methods=['POST'])
def submi():
	session['guess'] = int(request.form['guess'])
	if session['number'] > session['guess']:
		session['msg'] = 'TOO LOW LOW LOW APPLE BOTTOM'
	elif session['number'] < session['guess']:
		session['msg'] = '2 hi'
	else:
		session['msg'] = 'good job bruh :)'
	return render_template('index.html', msg=session['msg'],guess=session['guess'],number=session['number'])

app.run(debug=True)