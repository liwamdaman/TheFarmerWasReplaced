import Flags
from actions import *
from utils import rand_hat

N = get_world_size()
directions = [North, East, South, West]
vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def substance_needed(n = get_world_size(), maze_level = num_unlocked(Unlocks.Mazes)):
	substance = n * 2**(maze_level - 1)
	if Flags.DEBUG:
		print(substance)
	return substance
	
def simple():
	while True:
		plant(Entities.bush)
		substance = substance_needed(1)
		use_item(Items.Weird_Substance, substance)
		harvest()

def simple_drones():
	for i in range(max_drones() - 1):
		goto(i, 0)
		spawn_drone(simple)
	goto(max_drones() - 1, 0)
	simple()
	
def wall_follow(n = get_world_size(), recenter = False, greedy = False):
	x = get_pos_x()
	y = get_pos_y()
	if greedy:
		# try to move in the direction of the treasure initially
		dest_x, dest_y = measure()
		if abs(dest_x - x) > abs(dest_y - y):
			if dest_x > x:
				index = 1
			else:
				index = 3
		else:
			if dest_y > y:
				index = 0
			else:
				index = 2
		index += 1
	else:
		index = 0
	# Only move when maze is active
	while True:
		entity = get_entity_type()
		if entity == Entities.Treasure:
			# Recreate maze instead of reusing maze to prevent loops
			harvest()
			if recenter:
				goto(x, y)
			plant(Entities.bush)
			substance = substance_needed(n)
			use_item(Items.Weird_Substance, substance)
		if entity == Entities.Hedge:
			# Always try to move to the relative left, following the wall
			index = (index - 1) % 4
			while not move(directions[index]):
				# rotate CW and try again
				index = (index + 1) % 4
				
def bfs(n = get_world_size()):
	def build_adjacency():
		adj = {}
		visited = set()
		index = 0
		while len(visited) < n * n:
			x, y = get_pos_x(), get_pos_y()
			visited.add((x, y))
			adj[(x, y)] = []
			for i in range(4):
				if can_move(directions[i]):
					adj[(x, y)].append((x + vectors[i][0], y + vectors[i][1]))
			# Wall follow until the entire maze has been explored
			index = (index - 1) % 4
			while not move(directions[index]):
				index = (index + 1) % 4
		return adj
	adj = build_adjacency()
	#quick_print(adj)
	for m in range(300):
		start_x, start_y = get_pos_x(), get_pos_y()
		dest_x, dest_y = measure()
		queue = [[(start_x, start_y)]]
		read_ptr = 0
		visited = set()
		visited.add((start_x, start_y))
		while read_ptr < len(queue):
			path = queue[read_ptr]
			x, y = path[-1]
			read_ptr += 1
			if x == dest_x and y == dest_y:
				# We now have the optimal path, move drone
				for i, j in path:
					goto(i, j)
				substance = substance_needed(n)
				use_item(Items.Weird_Substance, substance)
				break
			for neighbour in adj[(x, y)]:
				if neighbour not in visited:
					visited.add(neighbour)
					queue.append(path + [neighbour])
	return

def maze():
	for n in range(N):
		goto(n, n)
		spawn_drone(wall_follow)
	plant(Entities.bush)
	substance = substance_needed()
	use_item(Items.Weird_Substance, substance)
	wall_follow()
	
def many_mazes():
	def start():
		# wait a moment for primary drone to exit incoming maze area
		do_a_flip()
		plant(Entities.bush)
		substance = substance_needed(5)
		use_item(Items.Weird_Substance, substance)
		#wall_follow(5, True, False)
		bfs(5)
	handles = []
	for i in range(2, 32, 5):
		for j in range(2, 32, 5):
			goto(i, j)
			handle = spawn_drone(start)
			if handle:
				handles.append(handle)
	start()
	for handle in handles:
		wait_for(handle)
			
def cheese():
	set_world_size(5)
	def polling():
		while True:
			if get_entity_type() == Entities.Treasure:
				if random() < 0.01:
					# create a new maze before we hit 300 uses
					harvest()
					plant(Entities.bush)
				substance = substance_needed(5)
				use_item(Items.Weird_Substance, substance)
	for i in range(5):
		for j in range(5):
			goto(i, j)
			spawn_drone(polling)
	plant(Entities.bush)
	substance = substance_needed(5)
	use_item(Items.Weird_Substance, substance)
	while True:
		if get_entity_type() == Entities.Treasure:
			if random() < 0.01:
				# create a new maze before we hit 300 uses
				harvest()
				plant(Entities.bush)
			substance = substance_needed(5)
			use_item(Items.Weird_Substance, substance)

if __name__ == "__main__":
	while True:
		clear()
		#print_substance_needed(32, 6)
		#simple_drones()
		#maze()
		#cheese()
		many_mazes()
	