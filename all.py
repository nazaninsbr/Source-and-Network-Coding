import huffman_coding
import convolutional_encoder
import noise
import viterbi_decoder

def pass_from_the_network(huffman_encoded_value):
	state_machine = convolutional_encoder.create_the_state_machine()
	encoded_version = convolutional_encoder.perform_convolutional_encoding(huffman_encoded_value, state_machine)
	return encoded_version

def main(input_string):
	print('Input Value: ', input_string)
	freq_mat = huffman_coding.read_the_freq_matrix()
	mapping = huffman_coding.create_mapping(freq_mat)
	huffman_encoded_value = huffman_coding.perform_huffman_coding(input_string, mapping)
	print('Huffman Encoded Value: ', huffman_encoded_value)
	on_the_other_side_of_the_network = pass_from_the_network(huffman_encoded_value)
	print('After passing the network: ', on_the_other_side_of_the_network)
	after_adding_noise = noise.add_noise(on_the_other_side_of_the_network)
	print('After adding noise: ', after_adding_noise)
	minimum_error, viterbi_decoded_value = viterbi_decoder.perform_viterbi_decoding(after_adding_noise)
	print('After Viterbi decoding: ', viterbi_decoded_value)
	final_result = huffman_coding.perform_huffman_decoding(viterbi_decoded_value, mapping)
	print('After huffman decoding: ', final_result)