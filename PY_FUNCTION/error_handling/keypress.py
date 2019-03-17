"""keypress - A module for detecting a single keypress """

try: 
    import find_msvcrt
	
	def getkey():
	    """Wait for keypress and return isngle character string"""
		return msvcrt.getch()

except ImportError:

    import sys
	import tty
	import termios

	def getkey():
	    """Wait for keypres and return single character string."""
		fd = sys.stdin.fileno()
		original_attributes = termios.tcgetattr(fd)
		try:
		    tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
		    termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
		return ch

		