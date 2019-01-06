import sys

def calculate_hamming_distance(x1, x2):
	dist = 0
	for xId in range(len(x1)):
		if not x1[xId]==x2[xId]:
			dist += 1
	return dist

def create_initial_PM_and_state_machine():
	# time step : {state: {resulting string : [initial string, next state]}}
	state_machine = {'00':{'00':['0', '00'], '11':['1', '10']}, '01':{'10':['0', '00'], '01':['1', '10']}, '10':{'11':['0', '01'], '00':['1', '11']}, '11':{'01':['0', '01'], '10':['1', '11']}}
	# 00 01 10 11
	return state_machine

def calculate_state_number(state):
	if state=='00':
		return 0
	if state=='01':
		return 1
	if state=='10':
		return 2
	else:
		return 3

def print_2d_list(l):
	for row in l:
		print(row)

def perform_backward_pass(forward_matrix):
	minimum_error = sys.maxsize
	place_to_go_back_from = -1
	for sId in range(4):
		if forward_matrix[sId][-1][2] < minimum_error:
			place_to_go_back_from = sId
			minimum_error = forward_matrix[sId][-1][2]

	time_step = len(forward_matrix[0]) -1
	result = ''
	while time_step>=0:
		result = forward_matrix[place_to_go_back_from][time_step][1] + result
		place_to_go_back_from = calculate_state_number(forward_matrix[place_to_go_back_from][time_step][0])
		time_step -= 1
	return result, minimum_error


def perform_forward_pass(state_machine, input_string):
	forward_matrix = []
	for s in state_machine.keys():
		row = []
		ind = 0
		while ind<=len(input_string)+1:
			# [where it came from, the bit value, the error]
			if ind==0 and (not s=='00'):
				row.append(['', '', sys.maxsize])
			else:
				row.append(['', '', 0])
			ind += 2 
		forward_matrix.append(row)
	time_step = 0
	ind = 0
	while ind<len(input_string):
		curr_2_bits = input_string[ind:ind+2]
		state_number = 0
		for state in state_machine.keys():
			for possible_coded_string in state_machine[state].keys():
				hamming_distance = calculate_hamming_distance(possible_coded_string, curr_2_bits)
				total_error = hamming_distance + forward_matrix[calculate_state_number(state)][time_step][2]
				if not forward_matrix[calculate_state_number(state_machine[state][possible_coded_string][1])][time_step+1][0]=='':
					if total_error<forward_matrix[calculate_state_number(state_machine[state][possible_coded_string][1])][time_step+1][2]:
						forward_matrix[calculate_state_number(state_machine[state][possible_coded_string][1])][time_step+1] = [state, state_machine[state][possible_coded_string][0], total_error]
				else:
					forward_matrix[calculate_state_number(state_machine[state][possible_coded_string][1])][time_step+1] = [state, state_machine[state][possible_coded_string][0], total_error]
		ind += 2
		time_step += 1

	decoded_value, minimum_error= perform_backward_pass(forward_matrix)
	return decoded_value, minimum_error


def perform_viterbi_decoding(input_string):
	state_machine = create_initial_PM_and_state_machine()
	decoded_value, minimum_error = perform_forward_pass(state_machine, input_string)
	return minimum_error, decoded_value

def main(input_string):
	minimum_error, decoded_value = perform_viterbi_decoding(input_string)
	print('Input Value: ', input_string)
	print('Minimum Error: ', minimum_error)
	print('Most Probable String: ', decoded_value)

