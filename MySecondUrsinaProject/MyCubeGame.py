from turtle import position
from numpy import block
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

grass_texture = load_texture('assets/grass_block.png')

stone_texture = load_texture('assets/stone_block.png')

brick_texture = load_texture('assets/brick_block.png')

dirt_texture  = load_texture('assets/dirt_block.png')

sky_texture   = load_texture('assets/skybox.png')


xlist = [6,7,8,9,10,11,12,13,14]

ylist = [1,2,3,4,5,6,7,8,9]

zlist = [6,7,8,9,10,11,12,13,14]


arm_texture   = load_texture('assets/arm_texture.png')



music   = Audio('Assets/Music.wav')

map_width , map_height =  10,10

layers = 1

destroy_sound   = Audio('assets/punch_sound.wav',loop = False, autoplay = False)

punch_sound   = Audio('assets/punch_sound.wav',loop = False, autoplay = False)

block_pick = 1

window.fps_counter.enabled = True

window.exit_button.visible = True

enemies = 1

scales = [1/2,3]

block_scale = scales[0]

def update():

	global block_pick

	if held_keys['left mouse'] or held_keys['right mouse']:
		hand.active()

	else:
		hand.passive()

	if held_keys['1']: block_pick = 1

	if held_keys['2']: block_pick = 2

	if held_keys['3']: block_pick = 3

	if held_keys['4']: block_pick = 4

	if held_keys['q']: app.destroy()
	
	if held_keys['m']: music.play()

	if held_keys['x']:
		xlist[0]+=1 ; 
		for z in range(len(xlist)):
			voxel = Voxel(position = (xlist[z],ylist[z],z),texture=stone_texture)

	if held_keys['z']:
		xlist[0]-=1 ; 
		for z in range(len(xlist)):
			voxel = Voxel(position = (xlist[z],ylist[z],z),texture=stone_texture)
	


class Voxel(Button):
	def __init__(self, position = (0,0,0), texture = grass_texture,scale = block_scale):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/block',
			origin_y = 0.5,
			texture = texture,
			color = color.color(0,0,9),
			scale = block_scale)



	def input(self,key):
		if self.hovered:

			if key == 'right mouse down':

				punch_sound.play()

				if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
				if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
				if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
				if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)




			if key == 'left mouse down':

				destroy_sound.play()

				destroy(self)






class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			color = color.blue,
			scale = 500,
			double_sided = True)



class Hand(Entity):
	def __init__(self):
		super().__init__(parent = camera.ui , model = 'assets/arm',texture = arm_texture,scale = 0.1,rotation = Vec3(150,-10,0),position = Vec2(15,10))

	def active(self):
		self.position = Vec2(0.3,-0.5)

	def passive(self):
		self.position = Vec2(0.4,-0.6)

	obj_texture = 'hero.png'

	for x in range(map_width):

		for y in range(layers):

			for z in range(map_height):

				voxel = Voxel(position = (x,y,z))


				for z in range(len(xlist)):
					voxel = Voxel(position = (xlist[z],ylist[z],zlist[z]),texture=stone_texture)
	

		for x in range(map_width):

			for y in range(layers):

				for z in range(map_height):
					z+=6
					voxel = Voxel(scale = block_scale,position = (x+map_height-1,y+map_height,z+map_height-1))

					z+=13
					block_scale+=1
					voxel = Voxel(scale = block_scale,position = (x+map_height-1,y+map_height,z+map_height-1))
				


			





player = FirstPersonController()

sky = Sky()

hand = Hand()

cube = Cube()



app.run()