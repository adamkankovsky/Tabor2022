import cv2
import pyzbar.pyzbar as pyzbar
from datetime import datetime
from time import sleep
import RPi.GPIO as GPIO

#width = 2592
#height = 1944

camera = cv2.VideoCapture(0)
#camera.set(3,width)
#camera.set(4,height)

def decodeCam(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(gray)
    print('reading...', end='\r')
    if barcodes:
        barcodeData = barcodes[0].data.decode()
        if barcodeData == "LTLovetin2022":
            print("well done")
            sleep(5)
        else:
            print("ouch")
            sleep(5)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
try:
    GPIO.output(11, GPIO.HIGH)  # Turn on
    sleep(2)  # Sleep for 2 second
    GPIO.output(11, GPIO.LOW)  # Turn off
    sleep(2)
    GPIO.output(11, GPIO.HIGH)  # Turn on
    sleep(2)  # Sleep for 2 second
    GPIO.output(11, GPIO.LOW)  # Turn off
    while True:
        # Read current frame
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        barcodes = pyzbar.decode(gray)
        if barcodes:
            barcodeData = barcodes[0].data.decode()
            if barcodeData == "LTLovetin2022":
                print("well done")
                sleep(5)
            else:
                print("ouch")
                sleep(5)
except KeyboardInterrupt:
    print('interrupted!')
