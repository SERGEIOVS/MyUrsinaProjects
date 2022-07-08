from base64 import b16decode
from cv2 import circle
from numpy import angle
from ursina import *
models = [

'cube',
'line',
'quad',
'wireframe_cube',
'plane',
'circle',
'diamond',
'wireframe_quad',
'sphere',
'icosphere',
'cube_uv_top',
'arrow',
'sky_dome',
'scale_gizmo'

]

Mymodel1 = models[0]

angle_x  = 25

angle_y = 45

angle_z = 0

colors = [
color.red,
color.yellow,
color.green,
color.blue,
color.orange,
color.white,
]
currentcolor = colors[0]

cube1 = Entity(model = Mymodel1, color = currentcolor)


class Cube1(Entity):
	
	def __init__(self):

		super().__init__(

			parent = scene,

			model = cube1,

			color = color.red,
		
			rotation = Vec3(angle_x,angle_y,angle_z)
		
)


# update is run every frame
def update():

	step = 20

	if held_keys['w']:
		cube1.rotation_x += step * time.dt

	if held_keys['s']:
		cube1.rotation_x -= step * time.dt

	if held_keys['a']:
		cube1.rotation_y += step * time.dt
	
	if held_keys['d']:
		cube1.rotation_y -= step * time.dt


# basic window
app = Ursina()


Cube1()

app.run()

"""

	if held_keys['a']:
		cube.x -= 5 * time.dt

	if held_keys['d']:
		cube.x += 5 * time.dt

	if held_keys['w']:
		circle.rotation_x += 20 * time.dt

	if held_keys['s']:
		circle.rotation_x -= 20 * time.dt

	if held_keys['a']:
		circle.rotation_y += 20 * time.dt
	
	if held_keys['d']:
		circle.rotation_y -= 20 * time.dt

models

'line'
'quad'
'wireframe_cube'
'plane'
'circle'
'diamond'
'wireframe_quad'
'sphere'
'cube'
'icosphere'
'cube_uv_top'
'arrow'
'sky_dome'
'scale_gizmo'

"""

