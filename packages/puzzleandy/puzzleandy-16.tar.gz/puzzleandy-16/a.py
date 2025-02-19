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

img = woman_1()
img = hue_shift(img,60)
#b = flip_vert(a)
#b = flip_hor(b)
#a = linear_light(a,b)
#lut = read('out.png')
lut = neutral_lut(64)
write(lut,'foo.png')
#b = apply_lut(a,lut,0.5)

mat3 = glm.mat3(
	1.0,0.0,0.0,
	0.0,0.0,0.0,
	0.0,0.0,1.0
);
c = color_mixer(img,mat3)
show(img)