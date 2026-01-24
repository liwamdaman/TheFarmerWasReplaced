from actions import *
from utils import rand_hat, wait_until_grown

N = get_world_size()
			
def plant_sunflowers():
	for i in range(N):
		for j in range(N):
			goto(i, j)
			smart_plant(Entities.Sunflower)
			
# Only scan grown sunflowers
def scan(petal_counts):
	for i in range(N):
		for j in range(N):
			goto(i, j)
			wait_until_grown()
			petals = measure()
			petal_counts[petals].append((i, j))
			
def collect(petal_counts):
	for i in range(15, 6, -1):
		for x, y in petal_counts[i]:
			goto(x, y)
			harvest()
			
def main():
	clear()
	while True:
		plant_sunflowers()
		petal_counts = []
		for _ in range(16):
			petal_counts.append([])
		scan(petal_counts)
		collect(petal_counts)
	
if __name__ == "__main__":
	main()