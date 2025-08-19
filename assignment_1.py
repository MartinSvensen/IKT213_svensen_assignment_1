import numpy as np
import cv2
img = cv2.imread('lena-1.png');
height, width, channels = img.shape[:3]
size = img.size
type =img.dtype
print(f"Height: {height} \nWidth: {width} \nChannels: {channels} \nSize: {size} \nType: {type}")
