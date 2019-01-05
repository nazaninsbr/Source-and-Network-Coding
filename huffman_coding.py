from helper import *
import copy
import sys

FREQ_MATRIX_PATH = './freq.mat'

def read_the_freq_matrix():
	freq_mat = read_mat_file(FREQ_MATRIX_PATH, "freq")
	return freq_mat.tolist()

def find_max_prob(prob_mat):
	max_prob = -sys.maxsize
	max_i = -1
	for i in range(len(prob_mat)):
		if prob_mat[i][0]>max_prob:
			max_prob = prob_mat[i][0]
			max_i = i
	prob_mat[max_i][0] = -sys.maxsize
	return prob_mat, max_i

def number_to_char_mapping(n):
	mapping = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
	return mapping[n]

def create_mapping(freq_mat):
	prob_mat = copy.deepcopy(freq_mat)
	mapping = {'a':'','b':'','c':'','d':'','e':'','f':'','g':'','h':'','i':'','j':'','k':'','l':'','m':'','n':'','o':'','p':'','q':'','r':'','s':'','t':'','u':'','v':'','w':'','x':'','y':'','z':''}
	prob_order, already_coded = [], []
	for _ in range(26):
		prob_mat, max_i = find_max_prob(prob_mat)
		prob_order.append(max_i)
	
	for ind in prob_order[:25]:
		c = number_to_char_mapping(ind)
		mapping[c] = mapping[c] + '0'
		already_coded.append(c)
		for x in mapping.keys():
			if not x in already_coded:
				mapping[x] = mapping[x] + '1'
	return mapping

def perform_huffman_coding(input_string, mapping):
	result = ''
	for c in input_string:
		result = result + mapping[c]
	return result

def perform_huffman_decoding(coded_value, mapping):
	result = ''
	while len(coded_value)>0:
		for val in mapping.keys():
			if coded_value.startswith(mapping[val]):
				result = result + val
				coded_value = coded_value[len(mapping[val]):]
	return result

def main(input_string):
	freq_mat = read_the_freq_matrix()
	print('Input String: '+input_string)
	mapping = create_mapping(freq_mat)
	coded_value = perform_huffman_coding(input_string, mapping)
	print('Coded Version: '+coded_value)
	decoded_value = perform_huffman_decoding(coded_value, mapping)
	print('Decoded Version: '+decoded_value)
	