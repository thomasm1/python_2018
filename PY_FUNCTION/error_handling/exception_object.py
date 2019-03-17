
import sys

def convert(s):
    '''Convert to an integer.'''
	try:
	    return int(s)
	except (ValueError, TypeError) as e:
	    print("Conversion erro: {}"\
		      .format(str(e)),
			  file=sys.stderr)
		# raise
        return -1
