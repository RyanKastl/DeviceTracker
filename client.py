import requests
import pyshark

point = "http://127.0.0.1:5000/tracker/"
key = "uh suh dude"

capture = pyshark.LiveCapture(interface='eth0')
capture.set_debug()

target = "7c:d9:5c:b4:dd:25"

for packet in capture.sniff_continuously():
	src = packet['ETH'].src
	dst = packet['ETH'].dst
	
	if (src == target or dst == target):
		data = {'mssg': 'Client 1 found Pixel 3 XL'}
		r = requests.post(url = point, data = data)
		print(r.text)



