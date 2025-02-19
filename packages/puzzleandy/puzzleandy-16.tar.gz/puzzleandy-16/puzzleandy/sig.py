import numpy as np
from .util import *

def sig(x,k):
	return (x-x*k)/(k-np.abs(x)*2*k+1)

def sig_contrast(x,c):
	k = remap(c,-1,1,1,-1)
	return (sig(2*x-1,k)+1)/2