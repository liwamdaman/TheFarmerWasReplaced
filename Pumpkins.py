from actions import *
from utils import rand_hat, benchmark
from drones import spawn_drones_horizontal

def replace_dead():
	check_queue = []
	read_ptr = 0
	for i in range(N):
		for j in range(N):
			check_queue.append((i,j))
	while read_ptr < len(check_queue):
		x, y = check_queue[read_ptr]
		read_ptr += 1
		goto(x, y)
		# wait until pumpkin is fully grown, if dead, then replace and move onto next.
		while get_entity_type() == Entities.Pumpkin and not can_harvest():
			rand_hat()
			smart_water()
		if get_entity_type() == Entities.Dead_Pumpkin:
			plant(Entities.Pumpkin)
			smart_water()
			check_queue.append((x, y))

def pumpkins():
	while True:
		for i in range(N):
			for j in range(N):
				goto(i, j)
				smart_plant(Entities.Pumpkin)
		replace_dead()
		# Should be able to harvest using single tile
		goto(0, 0)
		harvest()

def pumpkin_column(column = get_pos_x()):
	plant_pumpkin_column(column)
	replace_dead_column(column)

def plant_pumpkin_column(column):
	for j in range(N):
		goto(column, j)
		smart_plant(Entities.Pumpkin)

def replace_dead_column(column):
	check_queue = []
	read_ptr = 0
	for j in range(N):
		check_queue.append((column,j))
	while read_ptr < len(check_queue):
		x, y = check_queue[read_ptr]
		read_ptr += 1
		goto(x, y)
		# wait until pumpkin is fully grown, if dead, then replace and move onto next.
		while get_entity_type() == Entities.Pumpkin and not can_harvest():
			rand_hat()
			smart_water()
		if get_entity_type() == Entities.Dead_Pumpkin:
			plant(Entities.Pumpkin)
			smart_water()
			check_queue.append((x, y))
			

def pumpkins_parallel(time_limit = None, is_leaderboard = False):
	clear()
	start = get_time()
	while True:
		spawn_drones_horizontal(pumpkin_column)
		goto(0, 0)
		harvest()
		if time_limit and get_time() - start >= time_limit:
			break
		if is_leaderboard and num_items(Items.Pumpkin) >= 200000000:
			break

if __name__ == "__main__":
	clear()
	#set_world_size(6)
	N = get_world_size()
	#pumpkins()
	pumpkins_parallel(None, True)
	#benchmark(pumpkins_parallel)