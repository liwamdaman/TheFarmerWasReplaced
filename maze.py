import Flags
from actions import *

N = get_world_size()

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

if __name__ == "__main__":
	clear()
	#print_substance_needed(32, 6)
	simple_drones()
	