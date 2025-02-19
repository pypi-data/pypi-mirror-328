import cv2
from .convert import *

def get_hue(x):
	x = rgb_to_hsv(x)
	h,_,_ = cv2.split(x)
	return h

def set_hue(x,h):
	x = rgb_to_hsv(x)
	_,s,v = cv2.split(x)
	x = cv2.merge((h,s,v))
	return hsv_to_rgb(x)