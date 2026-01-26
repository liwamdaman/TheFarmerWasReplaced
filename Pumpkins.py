from actions import *
from utils import rand_hat

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

if __name__ == "__main__":
	clear()
	set_world_size(6)
	N = get_world_size()
	pumpkins()