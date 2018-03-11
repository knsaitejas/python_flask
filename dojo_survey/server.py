from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/view', methods=['POST'])
def views():
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comments']
	return render_template('results.html',name=name,location=location,language=language,comments=comment)

app.run(debug=True)

