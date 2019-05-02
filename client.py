import requests
import pyshark
import threading

reportURL = "http://192.168.1.6:5000/tracker/"
targetsURL = "http://192.168.1.6:5000/refresh/"
key = "api key here"
name = "Ryan's Apartment"

targets = {}

def refreshTargets(timerStop):
	res = requests.get(url = targetsURL)
	global targets
	targets = res.json()
	if not timerStop.is_set():
		threading.Timer(10, refreshTargets, [timerStop]).start()

timerStop = threading.Event()
refreshTargets(timerStop)

capture = pyshark.LiveCapture(interface='eth0')
capture.set_debug()


for packet in capture.sniff_continuously():
	src = packet['ETH'].src
	dst = packet['ETH'].dst
	
	if (src in targets):
		data = {'mssg': name + '/' + src}
		r = requests.post(url = reportURL, data = data)
		print(r.text)
	if (dst in targets):
		data = {'mssg': name + '/' + dst}
		r = requests.post(url = reportURL, data = data)
		print(r.text)



