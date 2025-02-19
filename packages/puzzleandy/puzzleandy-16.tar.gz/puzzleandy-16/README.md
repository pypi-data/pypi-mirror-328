```
import ctypes
import platform
from puzzleandy import *
if platform.system() == 'Windows':
	ctypes.windll.shcore.SetProcessDpiAwareness(1)

x = horses()
y = flip_hor(x)
z = multiply(y,x)
z = gamma(z,0.7)
show(z)
```