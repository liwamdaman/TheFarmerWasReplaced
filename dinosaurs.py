from actions import *

N = get_world_size()

# guaranteed approach, take the same path which travels the field
def traverse_field():
	while True:
		change_hat(Hats.Dinosaur_Hat)
		blocked = False
		while not blocked:
			for i in range(N):
				if i % 2 == 0:
					if not goto(i, N - 1, False):
						blocked = True
						break
				else:
					if not goto(i, 1, False):
						blocked = True
						break
			if not goto(N - 1, 0, False):
				blocked = True
				break
			if not goto(0, 0, False):
				blocked = True
				break
		change_hat(Hats.Straw_Hat)
		goto(0, 0)

# simple approach, just travel from point to point and harvest when blocked by own tail
def simple():
	while True:
		change_hat(Hats.Dinosaur_Hat)
		blocked = False
		while not blocked:
			next_x, next_y = measure()
			if not goto(next_x, next_y, False):
				blocked = True
				break
		change_hat(Hats.Straw_Hat)
		goto(0, 0)

if __name__ == "__main__":
	clear()
	#set_world_size(4)
	if num_items(Items.Cactus) < (N * N * 64):
		print("not enough cacti to support full snake run")
	traverse_field()
	#simple()
	