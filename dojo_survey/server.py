from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/view', methods=['POST'])
def views():
	name = request.form['name']
	if len(request.form['name']) <1 or len(request.form['comments']) <1 or len(request.form['comments']) >120:
		flash('Name or comments cannot be empty!')
		return redirect('/')
	else:
		flash("Success! Your name is {}".format(request.form['name']))
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comments']
	return render_template('results.html',name=name,location=location,language=language,comments=comment)

app.run(debug=True)

