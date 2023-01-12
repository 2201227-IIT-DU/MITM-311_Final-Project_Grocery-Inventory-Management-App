import cv2
from pyzbar.pyzbar import decode
import time
from playsound import playsound


DB = {}

class CodeScanner:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def set_window_size(self, width = 1920, height = 1080):
        self.cap.set(3, width)
        self.cap.set(4, height)

    def operate(self):
        camera = True
        while camera == True:
            success, frame = self.cap.read()

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
                    DB[productName] = 1
                
                else:
                    productName = DB[scannedCode]
                    DB[productName] += 1
                    print(f'{productName} x {DB[productName]}')
                    time.sleep(1.25)
                
            cv2.imshow('Scanner Camera', frame)
            cv2.waitKey(1)


codeScanner = CodeScanner()
codeScanner.set_window_size()
codeScanner.operate()
