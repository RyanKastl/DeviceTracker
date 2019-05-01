from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    testVar = "henlo"
    return render_template('home.html', testVar = testVar)

@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()