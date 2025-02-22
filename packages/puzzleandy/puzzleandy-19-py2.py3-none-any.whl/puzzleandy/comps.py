import cv2
from .convert import *

def get_hsl_h(x):
	x = rgb_to_hsl(x)
	H,_,_ = cv2.split(x)
	return H

def set_hsl_h(x,H):
	x = rgb_to_hsl(x)
	_,L,S = cv2.split(x)
	x = cv2.merge((H,L,S))
	return hsl_to_rgb(x)

def get_hsl_s(x):
	x = rgb_to_hsl(x)
	_,_,S = cv2.split(x)
	return S

def set_hsl_s(x,S):
	x = rgb_to_hsl(x)
	H,L,_ = cv2.split(x)
	x = cv2.merge((H,L,S))
	return hsl_to_rgb(x)

def get_hsl_l(x):
	x = rgb_to_hsl(x)
	_,L,_ = cv2.split(x)
	return L

def set_hsl_l(x,L):
	x = rgb_to_hsl(x)
	H,_,S = cv2.split(x)
	x = cv2.merge((H,L,S))
	return hsl_to_rgb(x)
