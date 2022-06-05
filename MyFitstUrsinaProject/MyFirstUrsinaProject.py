from base64 import b16decode
from cv2 import circle
from ursina import *

Mymodel1 = 'cube'

a1 = 25

b1 = 45

c1= 0

cube1 = Entity(model = Mymodel1, color = color.red)


class Cube1(Entity):
	
	def __init__(self):

		super().__init__(

			parent = scene,

			model = cube1,
			color = color.red,
			

			rotation = Vec3(a1,b1,c1)
		
)



# update is run every frame
def update():

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




"""

	if held_keys['b']:
		color = color.black

	if held_keys['s']:
		cube1.rotation_x -= 20 * time.dt

	if held_keys['a']:
		cube1.rotation_y += 20 * time.dt
	
	if held_keys['d']:
		cube1.rotation_y -= 20 * time.dt


# basic window
app = Ursina()


Cube1()

app.run()

"""

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

