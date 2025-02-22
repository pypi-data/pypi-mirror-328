from importlib.resources import files
from .basic import *
from .cmap_img import *

def _cmap(I,basename):
	path = files()/'cmaps'/basename
	M = read(path)
	return cmap_img(I,M)

def autumn(I):
	return _cmap(I,'autumn.jpg')

def bone(I):
	return _cmap(I,'bone.jpg')

def cividis(I):
	return _cmap(I,'cividis.jpg')

def cool(I):
	return _cmap(I,'cool.jpg')

def deep_green(I):
	return _cmap(I,'deep_green.jpg')

def hot(I):
	return _cmap(I,'hot.jpg')

def hsv(I):
	return _cmap(I,'hsv.jpg')

def inferno(I):
	return _cmap(I,'inferno.jpg')

def jet(I):
	return _cmap(I,'jet.jpg')

def magma(I):
	return _cmap(I,'magma.jpg')

def ocean(I):
	return _cmap(I,'ocean.jpg')

def parula(I):
	return _cmap(I,'parula.jpg')

def pink(I):
	return _cmap(I,'pink.jpg')

def plasma(I):
	return _cmap(I,'plasma.jpg')

def rainbow(I):
	return _cmap(I,'rainbow.jpg')

def spring(I):
	return _cmap(I,'spring.jpg')

def summer(I):
	return _cmap(I,'summer.jpg')

def turbo(I):
	return _cmap(I,'turbo.jpg')

def twilight(I):
	return _cmap(I,'twilight.jpg')

def twilight_shifted(I):
	return _cmap(I,'twilight_shifted.jpg')

def viridis(I):
	return _cmap(I,'viridis.jpg')

def winter(I):
	return _cmap(I,'winter.jpg')
