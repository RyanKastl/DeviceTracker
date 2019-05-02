from flask import Flask, render_template, redirect, url_for
from flask import request
from flask import jsonify
app = Flask(__name__)

key = "uh suh dude"

track = {
    'D1': {
    'addr' : 'Device1',
    'name' : 'Pixel 3 XL',
    'lastSeen' : 'N/A'
    }
}

def addDevice(device, name):
    dev = {
    'addr' : device,
    'name' : name,
    'lastSeen' : 'N/A'
    }
    return dev

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print("POSTING POSTING POSTING")
        data = request.form
        dev = addDevice(data['device'], data['name'])
        track[data['device']] = dev
        print("ADDED THE NEW DEVICE")
    return render_template('home.html', tracking = track)

@app.route('/about/')
def about():
    return render_template('about.html')

# Data should be in the form of "ClientID/Device"

@app.route('/tracker/', methods=['POST'])
def report():
    if request.method == 'POST':
        data = request.form
        report = data['mssg'].split("/")
        print(report)
        if (len(report) != 2):
            return 'Bad Format', 400
        track[report[1]]['lastSeen'] = report[0]
    return 'Received.', 200

@app.route('/refresh/')
def refresh():
    return jsonify(track)

@app.route('/delete/', methods=['POST'])
def delete():
    if request.method == 'POST':
        key = request.form['dKey']
        del track[key]
        return 'Device Deleted', 200
    return 'This is a POST endpoint', 200

# @app.route('/add/', methods=['POST'])
# def add():
#     print(request.form)
#     #dev = addDevice(device, name)
#     #track[device] = dev
#     return redirect(url_for('/'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    #app.run()