from sys import argv
from huffman_coding import main as run_huffman_code
from convolutional_encoder import main as run_convolutional_encoder
from viterbi_decoder import main as run_viterbi_decoder
from all import main as send_something

def main():
	if '--huffman' in argv:
		input_string = input()
		run_huffman_code(input_string)
	elif '--convolutional' in argv:
		input_string = input()
		run_convolutional_encoder(input_string)
	elif '--viterbi' in argv:
		input_string = input()
		run_viterbi_decoder(input_string)
	elif '--withInput' in argv:
		input_string = input()
		send_something(input_string)
	else:
		input_string = 'nazaninsabri'
		send_something(input_string)

if __name__ == '__main__':
	main()