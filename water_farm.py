from watering import water
from actions import *
from drones import *

clear()
N = get_world_size()

def water_column():
	x = get_pos_x()
	for y in range(N):
		goto(x, y)
		till()
		water()

spawn_drones_horizontal(water_column)