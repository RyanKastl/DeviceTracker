from flask import Flask, render_template
from flask import request
app = Flask(__name__)

key = "uh suh dude"

@app.route('/')
def home():
    testVar = "henlo"
    return render_template('home.html', testVar = testVar)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/tracker/', methods=['POST'])
def printData():
	if request.method == 'POST':
		data = request.form
		print(data)
	return 'sup', 200


if __name__ == '__main__':
    app.run()