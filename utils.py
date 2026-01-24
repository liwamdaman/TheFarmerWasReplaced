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
	
def rand_hat():
	hats = [
		Hats.Brown_Hat,
		Hats.Carrot_Hat,
		Hats.Gray_Hat,
		Hats.Green_Hat,
		Hats.Pumpkin_Hat,
		Hats.Purple_Hat,
		Hats.Straw_Hat,
		Hats.Sunflower_Hat,
		Hats.Traffic_Cone,
		Hats.Tree_Hat
	]
	change_hat(random_elem(hats))
	
def wait_until_grown():
	while not can_harvest():
		rand_hat()
	
def random_elem(list):
	index = random() * len(list) // 1
	return list[index]
	