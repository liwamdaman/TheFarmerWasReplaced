# Use rate limiting algo to distribute watering
# TODO: integrate water level threshold with rate limiting algo, balanced between the two

import Flags

water_restore_rate_by_level = {
	1: 0.1,
	2: 0.2,
	3: 0.4,
	4: 0.8,
	5: 1.6,
	6: 3.2,
	7: 6.4,
	8: 12.8,
	9: 25.6,
}

WATER_LEVEL_THRESHOLD = 0.8
INITIAL_TOKEN_BUCKET_SIZE = 10000

bucket = {
	"most_recent_call": -1,
	"tokens": INITIAL_TOKEN_BUCKET_SIZE
}

def smart_water():
	if get_water() > WATER_LEVEL_THRESHOLD:
		if Flags.DEBUG:
			quick_print("Skipped watering due to water level threshold. Current time is: " + str(get_time()))
		return False
	tokens = INITIAL_TOKEN_BUCKET_SIZE
	if bucket["most_recent_call"] != -1:
		elapsed = get_time() - bucket["most_recent_call"]
	else:
		elapsed = 0
	bucket["most_recent_call"] = get_time()
	bucket["tokens"] = min(INITIAL_TOKEN_BUCKET_SIZE, bucket["tokens"] + elapsed * water_restore_rate_by_level[num_unlocked(Unlocks.Watering)])
	if bucket["tokens"] < 1:
		if Flags.DEBUG:
			quick_print("Skipped watering due to rate limiting. Current time is: " + str(get_time()))
		return False
	use_item(Items.Water)
	bucket["tokens"] -= 1
	if Flags.DEBUG:
		quick_print("Current tokens remaining: " + str(bucket["tokens"]))
		quick_print("Current time is: " + str(get_time()))
	return True

def water():
	use_item(Items.Water)

if __name__ == "__main__":
	# Unit tests
	print("TODO")