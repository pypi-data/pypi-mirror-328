from importlib.resources import files
import moderngl
import numpy as np

def _contents(path):
	with open(path) as f:
		return f.read()

def cmap_img(I,M):
	Iw = I.shape[1]
	Ih = I.shape[0]
	Mw = M.shape[1]
	Mh = M.shape[0]
	shaders_path = files()/'shaders'
	vert_path = shaders_path/'default.vert'
	frag_path = shaders_path/'cmap_img.frag'
	ctx = moderngl.create_standalone_context()
	prog = ctx.program(
		_contents(vert_path),_contents(frag_path))
	prog['iChannel0'] = 0
	tex = ctx.texture((Iw,Ih),1,I.tobytes(),dtype='f4')
	tex.use(0)
	prog['iChannel1'] = 1
	tex = ctx.texture((Mw,Mh),3,M.tobytes(),dtype='f4')
	samp = ctx.sampler(False,texture=tex)
	samp.use(1)
	uni = prog['iResolution']
	uni.value = (Iw,Ih,1)
	col = ctx.texture((Iw,Ih),3,dtype='f4')
	fbo = ctx.framebuffer([col])
	fbo.use()
	fbo.clear(0,0,0,0)
	verts = ((-1,-1),(1,-1),(1,1),(-1,1))
	verts = np.array(verts, np.float32)
	vbo = ctx.buffer(verts.tobytes())
	vao = ctx.simple_vertex_array(prog,vbo,'pos')
	vao.render(moderngl.TRIANGLE_FAN)
	img = np.frombuffer(fbo.read(dtype='f4'),dtype=np.float32)
	img = img.reshape((Ih,Iw,3))
	return img