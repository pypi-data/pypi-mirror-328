import cv2
import numpy as np

def flip_hor(x):
	return cv2.flip(x,1)

def flip_vert(x):
	return cv2.flip(x,0)

def to_float(x):
	return (x/255).astype(np.float32)

def to_uint(x):
	return (x*255).astype(np.uint8)

def comps(x):
	match len(x.shape):
		case 2:
			return 1
		case _:
			return x.shape[2]

def to_bgr(x):
	x = to_uint(x)
	match comps(x):
		case 1:
			x = cv2.cvtColor(x,cv2.COLOR_GRAY2BGR)
		case 3:
			x = cv2.cvtColor(x,cv2.COLOR_RGB2BGR)
		case _:
			x = cv2.cvtColor(x,cv2.COLOR_RGBA2BGR)
	return to_float(x)

def read(path):
	x = cv2.imread(path)
	x = to_float(x)
	return to_bgr(x)

def write(x,path):
	x = to_bgr(x)
	cv2.imwrite(path,x)

def show(x):
	x = to_bgr(x)
	cv2.imshow('',x)
	cv2.waitKey()