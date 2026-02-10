from watering import smart_water
from actions import *
from utils import wait_until_grown
from drones import *
from utils import benchmark

N = get_world_size()

def harvest_and_plant_row():
	j = get_pos_y()
	for i in range(N):
		goto(i, j)
		wait_until_grown()
		harvest()
		companion, (x, y) = get_companion()
		while companion != Entities.Bush and y % 2 != 1:
			harvest()
			companion, (x, y) = get_companion()
		#smart_water() # Grass grows fast, not worth spending time watering

def main(time_limit = None, is_leaderboard = False):
	start = get_time()
	while True:
		spawn_drones_vertical_alternating_no_wait(harvest_and_plant_row)
		if time_limit and get_time() - start >= time_limit:
			break
		if is_leaderboard and num_items(Items.Hay) >= 2000000000:
			break

def setup():
	def plantBushes():
		j = get_pos_y()
		for i in range(N):
			goto(i, j + 1)
			plant(Entities.Bush)
	handles = spawn_drones_vertical_alternating_no_wait(plantBushes)
	#wait_for(handles[-1]) # Probably not needed

if __name__ == "__main__":
	clear()
	setup()
	main(None, True)
	#benchmark(main)