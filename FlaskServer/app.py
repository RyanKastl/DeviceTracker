from flask import Flask, render_template, redirect, url_for
from flask import request
from flask import jsonify
import threading

app = Flask(__name__)

key = "api key here"

track = {}

def addDevice(device, name, lastSeen = "N/A"):
    dev = {
    'addr' : device,
    'name' : name,
    'lastSeen' : lastSeen
    }
    return dev

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form
        dev = addDevice(data['device'].lower(), data['name'])
        track[data['device'].lower()] = dev
    return render_template('home.html', tracking = track)

@app.route('/about/')
def about():
    return render_template('about.html')

# Data should be in the form of "ClientID\Device"

@app.route('/tracker/', methods=['POST'])
def report():
    if request.method == 'POST':
        data = request.form
        report = data['mssg'].split("\\")
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

def loadTargets():
    try:
        f = open("targets.txt", "r")
        lines = f.readlines()

        for line in lines:
            t = line.strip().split("\\")
            dev = addDevice(t[0], t[1], t[2])
            track[t[0]] = dev
    except:
        return

def saveTargets(timerStop):
    f = open("targets.txt", "w+")
    for key, val in track.items():
        f.write(val['addr'] + "\\" + val['name'] + "\\" + val['lastSeen'] + "\r\n")
    f.close()

    if not timerStop.is_set():
        threading.Timer(10, saveTargets, [timerStop]).start()

timerStop = threading.Event()


if __name__ == '__main__':

    loadTargets()
    saveTargets(timerStop)

    app.run(host='0.0.0.0')
    #app.run()
