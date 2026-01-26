from utils import *
from actions import *
from drones import *

def plant_cacti():
	for i in range(N):
		for j in range(N):
			goto(i, j)
			smart_plant(Entities.Cactus)
			
def plant_row(row = get_pos_y()):
	for i in range(N):
		goto(i, row)
		smart_plant(Entities.Cactus)
			
# Using bubble sort
def sort_row(row = get_pos_y()):
	check_queue = []
	for i in range(N - 1):
		check_queue.append(i)
	while check_queue:
		x = check_queue.pop(0)
		goto(x, row)
		wait_until_grown()
		goto(x + 1, row)
		wait_until_grown()
		if measure(West) > measure():
			swap(West)
			if x > 0:
				check_queue.append(x - 1)

# Using bubble sort
def sort_column(column = get_pos_x()):
	check_queue = []
	for j in range(N - 1):
		check_queue.append(j)
	while check_queue:
		y = check_queue.pop(0)
		goto(column, y)
		wait_until_grown()
		goto(column, y + 1)
		wait_until_grown()
		if measure(South) > measure():
			swap(South)
			if y > 0:
				check_queue.append(y - 1)
	
def cactus():
	while True:
		plant_cacti()
		for row in range(N):
			sort_row(row)
		for column in range(N):
			sort_column(column)
		goto(N - 1, N - 1)
		harvest()
		
def cactus_parallel():
	spawn_drones_vertical(plant_row)
	spawn_drones_vertical(sort_row)
	spawn_drones_horizontal(sort_column)
	harvest()

if __name__ == "__main__":
	clear()
	# cactus()
	cactus_parallel()