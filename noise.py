import random

NOISE_PROBABILITY = 0.05

def add_noise(input_string):
	resulting_string = ''
	for ind in range(len(input_string)):
		r = random.uniform(0, 1)
		if r<NOISE_PROBABILITY:
			resulting_string = resulting_string + str(1 - int(input_string[ind]))
		else:
			resulting_string = resulting_string + input_string[ind]
	return resulting_string