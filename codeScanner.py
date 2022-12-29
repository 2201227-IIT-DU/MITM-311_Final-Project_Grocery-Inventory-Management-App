import cv2
from pyzbar.pyzbar import decode
import time
from playsound import playsound

cap = cv2.VideoCapture(0)
cap.set(3, 1600)
cap.set(4, 900)

DB = {}

camera = True
while camera == True:
    success, frame = cap.read()

    for code in decode(frame):
        # playsound('beep.mp3')
        scannedCode = code.data.decode('utf-8')
        if not scannedCode in DB:
            print(scannedCode)
            print('Product not found in DB')
            
            while True:
                productName = input('Enter new product name: ')
                if not productName == '':
                    break
            
            DB[scannedCode] = productName
        
        else:
            print(DB[scannedCode])
            time.sleep(1.25)
        
    cv2.imshow('Scanner Camera', frame)
    cv2.waitKey(1)

