from math import tan
import numpy as np
from .lerp import *

def clamp(x,m=0,M=1):
	return np.clip(x,m,M)

def pt_angle(x,px,py,t):
	return (x-px)*tan(t)+py

def remap(x,m1,M1,m2,M2):
	return lerp(unlerp(x,m1,M1),m2,M2)