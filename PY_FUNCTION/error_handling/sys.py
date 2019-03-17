

import sys

def main():
    try:
	    print(sqrt(9))
		print(sqrt(2))
		print(sqrt(-1))
		print("this never printed.")
	except ValueError as e:
	    print(e, file=sys.stderr)
	
	print("Program execution continues normally here")
	