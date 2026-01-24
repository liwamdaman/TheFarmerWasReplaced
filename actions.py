opposite = {
	East:West,
	West:East,
	North:South,
	South:North
}

def is_positioned(x, y):
	return x == get_pos_x() and y == get_pos_y()

def goto(x, y, N = get_world_size()):
	curr_x = get_pos_x()
	dx = x - curr_x
	x_dir = East
	if dx < 0:
		x_dir = opposite[x_dir]
	if abs(dx) > N//2:
		dx = N - abs(dx)
		x_dir = opposite[x_dir]
	for _ in range(abs(dx)):
		move(x_dir)
	curr_y = get_pos_y()
	dy = y - curr_y
	y_dir = North
	if dy < 0:
		y_dir = opposite[y_dir]
	if abs(dy) > N//2:
		dy = N - abs(dy)
		y_dir = opposite[y_dir]
	for _ in range(abs(dy)):
		move(y_dir)
	
def harvest_replace():
	crop = get_entity_type()
	harvest()
	if crop != Entities.Grass:
		plant(crop)	
	
def move_harvest_replace(x, y):
	if not is_positioned(x, y):
		goto(x, y)
	harvest_replace()
	
def smart_plant(entity):
	if entity in set([Entities.Carrot, Entities.Pumpkin, Entities.Sunflower]): 
		if get_ground_type() != Grounds.Soil:
			till()
	else:
		if get_ground_type() != Grounds.Grassland:
			till()
	plant(entity)
		
if __name__ == "__main__":
	# testing move() and visually validating results
	N = get_world_size()
	clear()
	goto(5,5)
	goto(3,3)
	goto(N//2+1,N//2+1)
	goto(N-2,N-2)
	# Should wrap around
	goto(3,3)
	# Should wrap around
	goto(N-1,N-1)