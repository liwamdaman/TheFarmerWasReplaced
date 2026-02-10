# Checker pattern is best for planting trees

from watering import smart_water
from actions import *
from utils import wait_until_grown
from drones import *
from utils import benchmark

N = get_world_size()
		
def harvest_and_plant_row(entity):
	j = get_pos_y()
	for i in range(N):
		if (i + j) % 2 == 0:
			goto(i, j + 1)
		else:
			goto(i, j)
		if get_entity_type() == entity:
			wait_until_grown()
		harvest()
		smart_plant(entity)
		companion, (x, y) = get_companion()
		while companion != Entities.Grass and (x + y) % 2 != 0:
			harvest()
			smart_plant(entity)
			companion, (x, y) = get_companion()
		smart_water()

def main(entity, time_limit = None, is_leaderboard = False):
	start = get_time()
	while True:
		spawn_drones_vertical_alternating_no_wait(fn_with_arg(harvest_and_plant_row, entity))
		if is_leaderboard and num_items(Items.Wood) >= 10000000000:
			break
		if time_limit and get_time() - start >= time_limit:
			break

def test(time_limit):
	main(Entities.Tree, time_limit)

if __name__ == "__main__":
	clear()
	main(Entities.Tree, None, True)
	#benchmark(test)