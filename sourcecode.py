#input your code
import cv2
import pyzbar.pyzbar as pyzbar
import numpy as np

def decode(image):
    for object in pyzbar.decode(image):
        print("DATA : ", object.data, '\n')
    return pyzbar.decode(image)
