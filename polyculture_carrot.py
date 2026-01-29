from watering import smart_water
from actions import *
from utils import wait_until_grown
from drones import *
from utils import benchmark

N = get_world_size()

def harvest_and_plant_row(entity):
	j = get_pos_y()
	for i in range(N):
		goto(i, j)
		if get_entity_type() == entity:
			wait_until_grown()
			harvest()
		smart_plant(entity)
		companion, (x, y) = get_companion()
		while companion != Entities.Grass and y % 2 != 1:
			harvest()
			smart_plant(entity)
			companion, (x, y) = get_companion()
		smart_water()

def main(entity, time_limit = None):
	start = get_time()
	while True:
		spawn_drones_vertical_alternating_no_wait(fn_with_arg(harvest_and_plant_row, entity))
		if time_limit and get_time() - start >= time_limit:
			break

def test(time_limit):
	main(Entities.Carrot, time_limit)

if __name__ == "__main__":
	clear()
	# use bush, tree, or carrots
	#main(Entities.Carrot)
	benchmark(test)