import Flags
from actions import *

def setup():
	if Flags.sunflowers_enabled:
		sun_x = 3
		sun_y = 4
		for i in range(sun_x):
			for j in range(sun_y):
				goto(i, j)
				till()
				plant(Entities.Sunflower)
		goto(0, 0)
	
	# Set up the grid with plants and soil types
	# Need to figure out proportions still
	N = get_world_size()
	wood = N//3
	carrot = N//5
	grass = N - wood - carrot
	for i in range(grass):
		move(East)
	for i in range(wood):
		for j in range(N):
			# we want to alternate between bush and tree in checkered pattern
			if (i+j) % 2 == 0:
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
			move(North)
		move(East)
	for i in range(carrot):
		for j in range(N):
			till()
			plant(Entities.Carrot)
			move(North)
		move(East)
	
def hat():
	# Make this randomly assigned once I unlock it
	change_hat(Hats.Traffic_Cone)