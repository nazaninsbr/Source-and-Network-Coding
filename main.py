from sys import argv
from huffman_coding import main as run_huffman_code
from convolutional_encoder import main as run_convolutional_encoder

def main():
	if '--huffman' in argv:
		input_string = input()
		run_huffman_code(input_string)
	elif '--convolutional' in argv:
		input_string = input()
		run_convolutional_encoder(input_string)

if __name__ == '__main__':
	main()