from importlib.resources import files
from .basic import *

def _tex(basename):
	path = files()/'tex'/basename
	return read(path)

def gradient():
	return _tex('gradient.png')

def tie_dye():
	return _tex('tie_dye.jpg')