# Implementation for purely polyculture-driven planting and harvesting
#Overall plan/flow:
# - arbitrary starting point (0,0) and plant a random plant
# - get companion coordinates, travel to it and plant the companion plant
#  - companion coordinates should be within a certain distance of each other
#  - check soil types and till() if needed
# - maintain list or set of coordinates for the plants in the polyculture, so that we can revisit them and see if they are ready to harvest
# - repeat this process, use an appropriate data structure + algo to optimize checking previous coordinates for harvesting as well as planting companions
#  - We might want to use some sort of prioritization as plants age, to ensure that can_harvest checks are efficiently successful
#  - in other words, trade-off distance optimization for harvest readiness optimization
# - Then, we can add in power + water + fertilizing

from actions import *

N = get_world_size()
clear()
do_a_flip()

harvest_candidates = [(0, 0)]
 # For now, just use a simple queue
while harvest_candidates:
	x, y = harvest_candidates.pop(0)
	goto(x, y)
	if can_harvest():
		harvest()
		plant(Entities.Grass)
	entity, (i, j) = get_companion()
	# To avoid getting stuck in a cycle of growing companions in a loop
	if (i, j) not in harvest_candidates:
		goto(i, j)
		smart_plant(entity)
		harvest_candidates.append((i,j))