import requests

point = "http://127.0.0.1:5000/tracker/"

key = "uh suh dude"

data = {'mssg': 'heyo'}

r = requests.post(url = point, data = data)

print(r.text)