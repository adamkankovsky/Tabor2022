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
try:
    GPIO.output(11, GPIO.HIGH)  # Turn on
    sleep(2)  # Sleep for 2 second
    GPIO.output(11, GPIO.LOW)  # Turn off
    sleep(2)
    GPIO.output(11, GPIO.HIGH)  # Turn on
    sleep(2)  # Sleep for 2 second
    GPIO.output(11, GPIO.LOW)  # Turn off
    while True:
        camera = cv2.VideoCapture(0)
        while True:
            # Read current frame
            ret, frame = camera.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            barcodes = pyzbar.decode(gray)
            if barcodes:
                barcodeData = barcodes[0].data.decode()
                if barcodeData == "LTLovetin2022":
                    camera.release()
                    cv2.destroyAllWindows()
                    print("well done")
                    playsound("/home/pi/Tabor2022/Tabor2022_Program/success.mp3")
                    sleep(10)
                    break
                else:
                    camera.release()
                    cv2.destroyAllWindows()
                    print("ouch")
                    playsound("/home/pi/Tabor2022/Tabor2022_Program/crash.mp3")
                    sleep(10)
                    break
except KeyboardInterrupt:
    print('interrupted!')
