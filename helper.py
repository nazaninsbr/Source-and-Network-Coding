import scipy.io as sio

def read_mat_file(path, field_to_return):
	content = sio.loadmat(path)
	return content[field_to_return]