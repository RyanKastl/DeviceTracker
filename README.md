# DeviceTracker
Device Tracker is a locally run server that can manage multiple clients (set up and run on machines such as Raspberry Pi's) that track a device's location through a secure and intuitive front-end. When a tracked device connects to a network that a client is monitoring, the client reports this information to the web server which is updated in real time.

## Infrastructure
- DeviceTracker runs a python Flask backend and an Angularjs frontend. 
- Requires authentication via cookies in a browser or an api key supplied by a client.
- Monitors devices by their MAC addresses.

## Setup
1. The web server requires Python3 and Flask.
2. The clients require Python3 and pyshark with Wireshark/tshark installed.
3. Supply your own api keys, password, and URL's in the app.py of the Flask server and client.py for the clients.
4. Simply run python3 FlaskServer/app.py to start up the web server.
5. With your clients set up on your preferred networks, run python3 client.py.
6. You may need to port forward your server port to your server machine.
7. Finally go to your web server ip address, login, and you're set!


# Alternate Description
# WatchYourBack2.0

This is the next level of security for the modern world. The basis of this product is to know where your device is at all times without having to rely on other companies to track for you. Have you ever lost your phone? I have - alot. 21Savage saw our product and added it to his new hit song - alot. And when it dies? You're out of luck. But with WatchYourBack2.0, your own server will know where your device is at all times. 

Background:

The device was created to be able to find someone's device on campus - but that was just too creepy. So plot twist -  we created a device that does something very similar but a little different. We set up clients at all the locations that would be useful - your office, headquarters, man cave, wherever you want basically and itll ping you whenever the device enters the area. It does this by parsing all the packets leaving these locations routers looking for your own device. When your device enters - ping your in. 

This application comes with its very own front end that'll keep track of your device at all times and let you know where it is. This device could be turned into a state of the art tracker to find whatever device you need. 

Future Use Cases:

product is still labeled Beta Edition - yes there will be more. If the average eye caught a glimpse of WireShark sniffing the packets on their network, they may lose their mind. But with our filter system, we can tell you whats reall up without making your eyes read the gibberish that only makes sense to the network junkies.
