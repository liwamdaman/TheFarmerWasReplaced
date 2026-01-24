# From some initial benchmarking, hay, wood, carrots gained.
# Initial polyculture implementation (level 1 polyculture): 602240, 2218368, 229248
# basic non-polyculture main loop: 250368, 1221120, 73637
# Roughly > 2x the output. Still have room to improve this using Water/Fertilizer for unluck tree edge cases,
# And also leveling up polyculture

from actions import *
from utils import *

N = get_world_size()
entities_to_plant = [
	Entities.Grass,
	Entities.Bush,
	Entities.Tree,
	Entities.Carrot
]

def polyculture(tick_limit = None):
	companion = {}
	tree_set = set()
	while True:
		for i in range(N):
			for j in range(N):
				goto(i, j)
				wait_until_grown()
				harvest_with_tree_set(tree_set)
				if (i, j) in companion and companion[(i, j)] != None:
					plant_with_tree_set(companion[(i, j)], tree_set)
					companion[(i, j)] = None
				else:
					# Plant smth random, but check for trees
					plant_with_tree_set(random_elem(entities_to_plant), tree_set, True)
				entity, (x, y) = get_companion()
				if isCompanionAhead(i, j, x, y):
					companion[(x, y)] = entity
				
				# Only used for performance testing with utils.benchmark()
				if tick_limit and get_tick_count() > tick_limit:
					return

def harvest_with_tree_set(tree_set):
	if get_entity_type() == Entities.Tree:
		x = get_pos_x()
		y = get_pos_y()
		tree_set.remove((x, y))
	harvest()

def plant_with_tree_set(entity, tree_set, check_neighbours = False):
	if entity == Entities.Tree:
		x = get_pos_x()
		y = get_pos_y()
		if check_neighbours:
			for neighbour in neighbours(x, y):
				if neighbour in tree_set:
					# plant grass instead
					smart_plant(Entities.Grass)
					return
		tree_set.add((x, y))
	smart_plant(entity)
	
					
# We only plant companions that are ahead, since we will always harvest in order
def isCompanionAhead(i, j, x, y):
	return (x > i or y > j) or (x < i and i - x > 3) 
		
if __name__ == "__main__":
	clear()
	do_a_flip()
	polyculture()
	#benchmark(polyculture)