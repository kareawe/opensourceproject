#input your code
import cv2
import pyzbar.pyzbar as pyzbar
import numpy as np

def decode(image):
    for object in pyzbar.decode(image):
        print("DATA : ", object.data, '\n')
    return pyzbar.decode(image)




def display(image, decoded):
    //draw a boundary around the decoded QR code and display the result as an image

if __name__ == '__main__':
    //read the image 'QR_gachon university.jpg' and use the decode function to decode the QR code
=======
def decode(image):
    for object in pyzbar.decode(image):
        print("DATA : ", object.data, '\n')
    return pyzbar.decode(image)
>>>>>>> main
