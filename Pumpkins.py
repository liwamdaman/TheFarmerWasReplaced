from actions import *
from utils import rand_hat

# Tries to create one big pumpkin with the entire grid
N = get_world_size()

def replace_dead():
	check_queue = []
	for i in range(N):
		for j in range(N):
			check_queue.append((i,j))
	while check_queue:
		x, y = check_queue.pop(0)
		goto(x, y)
		# wait until pumpkin is fully grown, if dead, then replace and move onto next.
		while get_entity_type() == Entities.Pumpkin and not can_harvest():
			rand_hat()
		if get_entity_type() == Entities.Dead_Pumpkin:
			plant(Entities.Pumpkin)
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
	pumpkins()