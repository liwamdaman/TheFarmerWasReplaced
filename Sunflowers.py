from actions import *
from utils import rand_hat, wait_until_grown
from drones import *

N = get_world_size()
			
def plant_sunflowers():
	for i in range(N):
		plant_sunflower_column(i)

def plant_sunflower_column(column = get_pos_x()):
	for j in range(N):
		goto(column, j)
		smart_plant(Entities.Sunflower)

# Only scan grown sunflowers
def scan_column(column = get_pos_x()):
	petal_counts = init_counts()
	for j in range(N):
		goto(column, j)
		wait_until_grown()
		petals = measure()
		petal_counts[petals].append((column, j))
	return petal_counts
		
def merge_counts(counts):
	counts_by_column = init_counts()
	for i in range(15, 6, -1):
		for _ in range(N):
			counts_by_column[i].append([])
	for count in counts:
		for key in count:
			for x, y in count[key]:
				counts_by_column[key][x].append((x, y))
	return counts_by_column
			
def collect(counts_by_column):
	for i in range(15, 6, -1):
		spawn_drones_horizontal(fn_with_arg(collect_by_column, counts_by_column[i]))
			
def collect_by_column(counts_by_column):
	column = get_pos_x()
	harvest_list = counts_by_column[column]
	for x, y in harvest_list:
		goto(x, y)
		harvest()
		
def init_counts():
	petal_counts = {}
	for n in range(7, 16):
		petal_counts[n] = []
	return petal_counts
			
def main(isLeaderboard = False):
	clear()
	while True:
		spawn_drones_horizontal(plant_sunflower_column)
		counts = spawn_drones_horizontal(scan_column)
		counts_by_column = merge_counts(counts)
		collect(counts_by_column)
		if isLeaderboard and num_items(Items.Power) >= 100000:
			break
	
if __name__ == "__main__":
	main(True)