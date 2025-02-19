from importlib.resources import files
from .basic import *

def _photo(basename):
	path = files()/'photos'/basename
	return read(path)

def bones():
	return _photo('bones.jpg')

def building():
	return _photo('building.jpg')

def horses():
	return _photo('horses.jpg')

def mountains():
	return _photo('mountains.jpg')

def pelican():
	return _photo('pelican.jpg')

def subway():
	return _photo('subway.jpg')

def woman_1():
	return _photo('woman_1.jpg')

def woman_2():
	return _photo('woman_2.jpg')