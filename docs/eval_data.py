import re

def get_data_type(value):
	"""
	123
	123.321
	1.
	.2
	"""

	numeric_regex = r"^(\d+)|(\d+\.\d+)|(\d*\.\d+)|(\d+\.\d*)$"
	
	if re.match(r"^((\d+)|(\d+\.\d+)|(\d*\.\d+)|(\d+\.\d*))$", str(value)):
		_type = 'numeric';
	else:
		_type = 'string';

	return _type;


# To work and test the working of eval function
def test_eval():
	s = "'Py Gen'"
	s2 = "12"
	s3 = "12.0"
	s4 = "'New version'"

	print(type(s))
	print(type(s2))
	print(type(s3))
	print(type(s4))


	print(type(eval(s)))
	print(type(eval(s2)))
	print(type(eval(s3)))
	print(type(eval(s4)))


def test():
	arr = [12, 12.34, .67, 34., '12', '34.78', '78.', '.99', 'tiger', '12s', 'tiger56']
	for n in arr:
		print(get_data_type(n))

test()