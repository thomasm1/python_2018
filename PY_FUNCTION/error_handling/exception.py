''' Module for demoing exceptions 
from exceptional import convert
convert("33")
333
'''

def convert(s):
    '''Convert to an integer'''
	x = -1
	try:
	    x = int(s)
		print("Conversion success! x =", x) 
	except (ValueError, TypeError):
	    print("Conversion failed!")
		#pass
	return x