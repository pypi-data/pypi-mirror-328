from importlib.resources import files
import moderngl
import numpy as np

def _contents(path):
	with open(path) as f:
		return f.read()

def cmap_stops(
	I,col_stops,col_mids,alpha_stops,alpha_mids):
	w = I.shape[1]
	h = I.shape[0]
	shaders_path = files()/'shaders'
	vert_path = shaders_path/'default.vert'
	frag_path = shaders_path/'cmap_stops.frag'
	ctx = moderngl.create_standalone_context()
	prog = ctx.program(
		_contents(vert_path),_contents(frag_path))
	prog['iChannel0'] = 0
	tex = ctx.texture((w,h),1,I.tobytes(),dtype='f4')
	tex.use(0)
	uni = prog['iResolution']
	uni.value = (w,h,1)
	prog['num_col_stops'] = len(col_stops)
	for i in range(len(col_stops)):
		prog[f'col_stops[{i}].loc'] = col_stops[i].loc
		col = col_stops[i].col
		prog[f'col_stops[{i}].col'] = (col[0], col[1], col[2])
	val = np.array(col_mids, np.float32)
	val = np.resize(val, 9)
	prog['col_mids'] = val
	prog['num_alpha_stops'] = len(alpha_stops)
	for i in range(len(alpha_stops)):
		prog[f'alpha_stops[{i}].loc'] = alpha_stops[i].loc
		prog[f'alpha_stops[{i}].alpha'] = alpha_stops[i].alpha
	val = np.array(alpha_mids, np.float32)
	val = np.resize(val, 9)
	prog['alpha_mids'] = val
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