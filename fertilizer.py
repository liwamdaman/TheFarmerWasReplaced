from utils import wait_until_grown
from watering import smart_water

# used for farming weird substance. Careful, this uses a lot of fertilizer
def get_weird():
	while True:
		smart_water()
		plant(Entities.Tree)
		use_item(Items.Fertilizer)
		wait_until_grown()
		harvest()
		
def fertilize():
	use_item(Items.Fertilizer)

if __name__ == "__main__":
	clear()
	get_weird()