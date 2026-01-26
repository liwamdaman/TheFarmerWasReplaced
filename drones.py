N = get_world_size()
from actions import goto

def spawn_drones_vertical(fn, column = 0):
	goto(column, 0)
	handles = []
	for j in range(N - 1):
		goto(column, j)
		handles.append(spawn_drone(fn))
	goto(column, N - 1)
	res = fn()
	results = []
	for handle in handles:
		results.append(wait_for(handle))
	results.append(res)
	return results

def spawn_drones_horizontal(fn, row = 0):
	goto(0, row)
	handles = []
	for i in range(N - 1):
		goto(i, row)
		handles.append(spawn_drone(fn))
	goto(N - 1, row)
	res = fn()
	results = []
	for handle in handles:
		results.append(wait_for(handle))
	results.append(res)
	return results
	
def fn_with_arg(fn, arg):
	def func():
		fn(arg)
	return func