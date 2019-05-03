import requests
import pyshark
import threading

# Replace this info with your own.
reportURL = "http://192.168.1.6:5000/tracker/"
targetsURL = "http://192.168.1.6:5000/refresh/"
key = "api key here"
auth = {'apiKey': key}

# name must NOT include any "\"s.
name = "Ryan's Apartment"

targets = {}

def refreshTargets(timerStop):
	try:
		res = requests.post(url = targetsURL, data = auth)
		global targets
		targets = res.json()
	except:
		print("No connection to server.")
	if not timerStop.is_set():
		threading.Timer(10, refreshTargets, [timerStop]).start()

timerStop = threading.Event()
refreshTargets(timerStop)

capture = pyshark.LiveCapture(interface='eth0')
capture.set_debug()


for packet in capture.sniff_continuously():
	src = packet['ETH'].src
	dst = packet['ETH'].dst
	
	try:
		if (src in targets):
			data = {'apiKey': key,
					'mssg': name + '\\' + src}
			r = requests.post(url = reportURL, data = data)
			print(r.text)
		if (dst in targets):
			data = {'apiKey': key,
					'mssg': name + '\\' + dst}
			r = requests.post(url = reportURL, data = data)
			print(r.text)
	except:
		print("No connection to server.")



