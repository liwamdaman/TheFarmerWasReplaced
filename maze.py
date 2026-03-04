import Flags
from actions import *
from utils import rand_hat

N = get_world_size()
directions = [North, East, South, West]

def substance_needed(n = get_world_size(), maze_level = num_unlocked(Unlocks.Mazes)):
	substance = n * 2**(maze_level - 1)
	if Flags.DEBUG:
		print(substance)
	return substance
	
def simple():
	while True:
		plant(Entities.bush)
		substance = substance_needed(1)
		use_item(Items.Weird_Substance, substance)
		harvest()

def simple_drones():
	for i in range(max_drones() - 1):
		goto(i, 0)
		spawn_drone(simple)
	goto(max_drones() - 1, 0)
	simple()
	
def wall_follow(n = get_world_size(), recenter = False, greedy = False):
	x = get_pos_x()
	y = get_pos_y()
	if greedy:
		# try to move in the direction of the treasure initially
		dest_x, dest_y = measure()
		if abs(dest_x - x) > abs(dest_y - y):
			if dest_x > x:
				index = 1
			else:
				index = 3
		else:
			if dest_y > y:
				index = 0
			else:
				index = 2
		index += 1
	else:
		index = 0
	# Only move when maze is active
	while True:
		entity = get_entity_type()
		if entity == Entities.Treasure:
			# Recreate maze instead of reusing maze to prevent loops
			harvest()
			if recenter:
				goto(x, y)
			plant(Entities.bush)
			substance = substance_needed(n)
			use_item(Items.Weird_Substance, substance)
		if entity == Entities.Hedge:
			# Always try to move to the relative left, following the wall
			index = (index - 1) % 4
			while not move(directions[index]):
				# rotate CW and try again
				index = (index + 1) % 4

def maze():
	for n in range(N):
		goto(n, n)
		spawn_drone(wall_follow)
	plant(Entities.bush)
	substance = substance_needed()
	use_item(Items.Weird_Substance, substance)
	wall_follow()
	
def many_mazes():
	def start():
		# wait a moment for primary drone to exit incoming maze area
		do_a_flip()
		plant(Entities.bush)
		substance = substance_needed(5)
		use_item(Items.Weird_Substance, substance)
		wall_follow(5, True, False)
	for i in range(2, 32, 5):
		for j in range(2, 32, 5):
			goto(i, j)
			spawn_drone(start)
	start()
			
def cheese():
	set_world_size(5)
	def polling():
		while True:
			if get_entity_type() == Entities.Treasure:
				if random() < 0.01:
					# create a new maze before we hit 300 uses
					harvest()
					plant(Entities.bush)
				substance = substance_needed(5)
				use_item(Items.Weird_Substance, substance)
	for i in range(5):
		for j in range(5):
			goto(i, j)
			spawn_drone(polling)
	plant(Entities.bush)
	substance = substance_needed(5)
	use_item(Items.Weird_Substance, substance)
	while True:
		if get_entity_type() == Entities.Treasure:
			if random() < 0.01:
				# create a new maze before we hit 300 uses
				harvest()
				plant(Entities.bush)
			substance = substance_needed(5)
			use_item(Items.Weird_Substance, substance)

if __name__ == "__main__":
	clear()
	#print_substance_needed(32, 6)
	#simple_drones()
	#maze()
	#cheese()
	many_mazes()
	