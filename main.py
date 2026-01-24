import utils
import Flags
from actions import *

clear()

# common vars
N = get_world_size()

utils.setup()

# main control loop
def main(tick_limit): 
	while True:
		if Flags.sunflowers_enabled:
			# Assumes that sunflowers are all fully grown
			max_petals = 0
			max_petals_loc = [0,0]
			sun_x = 3
			sun_y = 4
			for i in range(sun_x):
				for j in range(sun_y):
					goto(i, j)
					if measure() > max_petals:
						max_petals = measure()
						max_petals_loc = [i, j]
			move_harvest_replace(max_petals_loc[0], max_petals_loc[1])
				
		for i in range(N):
			for j in range(N):
				move_harvest_replace(i, j)
				
		# Only used for performance testing with utils.benchmark()
			if tick_limit and get_tick_count() > tick_limit:
				return
			
if __name__ == "__main__":
	main()
	#utils.benchmark(main)