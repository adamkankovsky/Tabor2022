#!/usr/bin/env python
import os

import cv2
import pyzbar.pyzbar as pyzbar
from time import sleep
import RPi.GPIO as GPIO
from playsound import playsound

#width = 2592
#height = 1944

#camera = cv2.VideoCapture(0)
#camera.set(3,width)
#camera.set(4,height)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
try:
    GPIO.output(11, GPIO.HIGH)  # Turn on
    GPIO.output(12, GPIO.HIGH)  # Turn on
    sleep(2)  # Sleep for 2 second
    GPIO.output(11, GPIO.LOW)  # Turn off
    GPIO.output(12, GPIO.LOW)  # Turn off
    sleep(2)
    GPIO.output(11, GPIO.HIGH)  # Turn on
    GPIO.output(12, GPIO.HIGH)  # Turn on
    sleep(2)  # Sleep for 2 second
    GPIO.output(11, GPIO.LOW)  # Turn off
    GPIO.output(12, GPIO.LOW)  # Turn off
    while True:
        camera = cv2.VideoCapture(0)
        while True:
            # Read current frame
            ret, frame = camera.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            barcodes = pyzbar.decode(gray)
            if barcodes:
                barcodeData = barcodes[0].data.decode()
                if isinstance(barcodeData, int):
			if 0 <= int(barcodeData) <= 35:
                    		camera.release()
                    		cv2.destroyAllWindows()
                    		print("well done")
                    		file = "/home/pi/Tabor2022/Tabor2022_Program/success.mp3"
                    		os.system("mpg123 " + file)
                    		#playsound('/home/pi/Tabor2022/Tabor2022_Program/success.mp3')
                    		sleep(10)
                    		break
                	else:
                    		camera.release()
                    		cv2.destroyAllWindows()
                    		print("ouch")
                    		file = "/home/pi/Tabor2022/Tabor2022_Program/crash.mp3"
                    		os.system("mpg123 " + file)
                    		#playsound('/home/pi/Tabor2022/Tabor2022_Program/crash.mp3')
                    		sleep(10)
                    		break
		else:
			camera.release()
                        cv2.destroyAllWindows()
                        print("ouch")
                        file = "/home/pi/Tabor2022/Tabor2022_Program/cr>
                        os.system("mpg123 " + file)
                        #playsound('/home/pi/Tabor2022/Tabor2022_Progra>
                        sleep(10)
                        break

except KeyboardInterrupt:
    print('interrupted!')
