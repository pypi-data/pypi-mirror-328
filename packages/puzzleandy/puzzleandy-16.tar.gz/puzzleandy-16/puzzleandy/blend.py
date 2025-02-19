from importlib.resources import files
import moderngl
import numpy as np

def _contents(path):
	with open(path) as f:
		return f.read()

def _blend(b,t,mode):
	w = b.shape[1]
	h = b.shape[0]
	shaders_path = files()/'shaders'
	vert_path = shaders_path/'default.vert'
	frag_path = shaders_path/f'{mode}.frag'
	ctx = moderngl.create_standalone_context()
	prog = ctx.program(
		_contents(vert_path),_contents(frag_path))
	prog['iChannel0'] = 0
	tex = ctx.texture((w,h),3,b.tobytes(),dtype='f4')
	tex.use(0)
	prog['iChannel1'] = 1
	tex = ctx.texture((w,h),3,t.tobytes(),dtype='f4')
	tex.use(1)
	uni = prog['iResolution']
	uni.value = (w,h,1)
	col = ctx.texture((w,h),3,dtype='f4')
	fbo = ctx.framebuffer([col])
	fbo.use()
	fbo.clear(0,0,0,0)
	verts = ((-1,-1),(1,-1),(1,1),(-1,1))
	verts = np.array(verts, np.float32)
	vbo = ctx.buffer(verts.tobytes())
	vao = ctx.simple_vertex_array(prog,vbo,'pos')
	vao.render(moderngl.TRIANGLE_FAN)
	img = np.frombuffer(fbo.read(dtype='f4'),dtype=np.float32)
	img = img.reshape((h,w,3))
	return img

# normal group

def normal(b,t):
	return _blend(b,t,'normal')

# darken group

def darken(b,t):
	return _blend(b,t,'darken')

def multiply(b,t):
	return _blend(b,t,'multiply')

def color_burn(b,t):
	return _blend(b,t,'color_burn')

def linear_burn(b,t):
	return _blend(b,t,'linear_burn')

def darker_color(b,t):
	return _blend(b,t,'darker_color')

# lighten group

def lighten(b,t):
	return _blend(b,t,'lighten')

def screen(b,t):
	return _blend(b,t,'screen')

def color_dodge(b,t):
	return _blend(b,t,'color_dodge')

def linear_dodge(b,t):
	return _blend(b,t,'linear_dodge')

def lighter_color(b,t):
	return _blend(b,t,'lighter_color')

# contrast group

def overlay(b,t):
	return hard_light(t,b)

def soft_light(b,t):
	return _blend(b,t,'soft_light')

def hard_light(b,t):
	return _blend(b,t,'hard_light')

def vivid_light(b,t):
	return _blend(b,t,'vivid_light')

def linear_light(b,t):
	return _blend(b,t,'linear_light')

def pin_light(b,t):
	return _blend(b,t,'pin_light')

def hard_mix(b,t):
	return np.floor(b+t)

# inversion group

def difference(b,t):
	return _blend(b,t,'difference')

def exclusion(b,t):
	return _blend(b,t,'exclusion')

# cancelation group

def subtract(b,t):
	return _blend(b,t,'subtract')

def divide(b,t):
	return _blend(b,t,'divide')

# component group

def hue(b,t):
	b = cv2.cvtColor(b,cv2.COLOR_RGB2HLS)
	t = cv2.cvtColor(t,cv2.COLOR_RGB2HLS)
	bH,bL,bS = cv2.split(b)
	tH,tL,tS = cv2.split(t)
	img = cv2.merge((bH,tL,tS))
	return cv2.cvtColor(img,cv2.COLOR_HLS2RGB)

def saturation(b,t):
	b = cv2.cvtColor(b,cv2.COLOR_RGB2HLS)
	t = cv2.cvtColor(t,cv2.COLOR_RGB2HLS)
	bH,bL,bS = cv2.split(b)
	tH,tL,tS = cv2.split(t)
	img = cv2.merge((tH,tL,bS))
	return cv2.cvtColor(img,cv2.COLOR_HLS2RGB)

def color(b,t):
	b = cv2.cvtColor(b,cv2.COLOR_RGB2HLS)
	t = cv2.cvtColor(t,cv2.COLOR_RGB2HLS)
	bH,bL,bS = cv2.split(b)
	tH,tL,tS = cv2.split(t)
	img = cv2.merge((tH,bL,tS))
	return cv2.cvtColor(img,cv2.COLOR_HLS2RGB)

def luminosity(b,t):
	return color(t,b)