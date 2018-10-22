import os 
from time import sleep

def mymail():
	return

def takesnap():
	os.system("fswebcam -F 4 /home/dl120/harsha/camera/web.jpg")
	return

for i in range(5):
	takesnap()
	mymail()
	sleep(5)