def create_the_state_machine():
	# state : {input: [code value , next state]}
	state_machine = {'00': {'0':['00', '00'], '1':['11', '10']},'10': {'1':['00', '11'], '0':['11', '01']},'01': {'0':['10', '00'], '1':['01', '10']},'11': {'0':['01', '01'], '1':['10', '11']}}
	return state_machine

def perform_convolutional_encoding(input_string, state_machine):
	result = ''
	curr_state = '00'
	ind = 0
	while ind<len(input_string):
		result = result + state_machine[curr_state][input_string[ind]][0]
		curr_state = state_machine[curr_state][input_string[ind]][1]
		ind += 1
	return result

def main(input_string):
	state_machine = create_the_state_machine()
	encoded_version = perform_convolutional_encoding(input_string, state_machine)
	print('Input Value: ', input_string)
	print('Coded Value: ', encoded_version)