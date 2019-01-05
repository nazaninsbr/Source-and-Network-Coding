from sys import argv
from huffman_coding import main as run_huffman_code

def main():
	if '--huffman' in argv:
		input_string = input()
		run_huffman_code(input_string)

if __name__ == '__main__':
	main()