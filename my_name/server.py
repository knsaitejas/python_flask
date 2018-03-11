from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def submitted():
	# print 'Got post info'
	x = request.form['name']
	print x
	return redirect('/')

app.run(debug=True)