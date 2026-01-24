from utils import *
from actions import *

def plant_cacti():
	for i in range(N):
		for j in range(N):
			goto(i, j)
			smart_plant(Entities.Cactus)
			
# Using bubble sort
def sort_row(row):
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
def sort_column(column):
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
	plant_cacti()
	for row in range(N):
		sort_row(row)
	for column in range(N):
		sort_column(column)
	goto(N - 1, N - 1)
	harvest()

if __name__ == "__main__":
	clear()
	cactus()