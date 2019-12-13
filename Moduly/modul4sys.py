"""Nasz czwarty moduł. """

#print('Jestem:', __name__)

def minmax(test, *args):
	res = args[0]
	for arg in args[1:]:
		if test(arg, res):
			res = arg
	return res
	
def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y

if __name__ == '__main__':
	import sys
	
	if len(sys.argv) < 2: 
		print("Modyl {} wymaga podania listy argumentow.".format(sys.argv[0]))
	else:
		print("wynik=",minmax(lessthan, *sys.argv[1:]))
		print("wynik=",minmax(grtrthan, *sys.argv[1:]))
