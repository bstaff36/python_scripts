import sys
arg1 = float(sys.argv[1])
arg2 = float(sys.argv[2])
arg3 = float(sys.argv[3])

def mypoly(arg1):
	print("My polynomial is: " + str(int(arg1**2 + 2*arg1 + 1)))

def exchange(arg2, rate=1.5):
	value=arg2*arg3
	print("The converted value of %3.2f dollars is %3.2f" %(arg2, value))

mypoly(arg1)
exchange(arg2, arg3)
