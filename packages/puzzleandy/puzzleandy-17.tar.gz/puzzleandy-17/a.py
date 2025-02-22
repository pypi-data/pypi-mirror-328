import ctypes
import glm
import platform
from puzzleandy import *
if platform.system() == 'Windows':
	ctypes.windll.shcore.SetProcessDpiAwareness(1)

def hue_shift(x,s):
	h = get_hue(x)
	h = np.mod(h+s,360)
	return set_hue(x,h)

def rgb_to_gray(I):
	return cv2.cvtColor(I,cv2.COLOR_RGB2GRAY)

class ColStop:
	def __init__(self, loc, col):
		self.loc = loc
		self.col = col

class AlphaStop:
	def __init__(self, loc, alpha):
		self.loc = loc
		self.alpha = alpha

col_stops = [
	ColStop(0, glm.vec3(0, 0, 0) / 255),
	ColStop(1, glm.vec3(43, 177, 236) / 255)
]
col_mids = [0.68]
alpha_stops = [
	AlphaStop(0, 1),
	AlphaStop(1, 1)
]
alpha_mids = [0.5]

x = pelican()
y = flip_hor(x)
y = flip_vert(y)
z = hue(x,y)
#t = 1-b
#I = col_burn(b,t)
#I = disc_col_map(I,col_stops,col_mids,alpha_stops,alpha_mids)
show(z)