from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninjas')
def ninjas():
	return render_template('ninja.html')

@app.route('/<color>')
def turtle(color):
	if color == 'blue':
		return render_template('blue.html')
	elif color == 'red':
		return render_template('red.html')
	elif color == 'orange':
		return render_template('orange.html')
	elif color == 'purple':
		return render_template('purple.html')
	else:
		return render_template('megan_fox.html')


app.run(debug=True)