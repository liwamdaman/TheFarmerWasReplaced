# Tries to create one big pumpkin with the entire grid
N = get_world_size()

def replace_dead():
	dead_detected = True
	while dead_detected:
		dead_detected = False
		for i in range(N):
			for j in range(N):
				if get_entity_type() == Entities.Dead_Pumpkin:
					plant(Entities.Pumpkin)
					dead_detected = True
				move(North)
			move(East)

def pumpkins():
	for i in range(N):
		for j in range(N):
			till()
			move(North)
		move(East)
	while True:
		replace_dead()
		# Should be able to harvest using single tile
		harvest()
		for i in range(N):
			for j in range(N):
				plant(Entities.Pumpkin)
				move(North)
			move(East)

if __name__ == "__main__":
	clear()
	pumpkins()