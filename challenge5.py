import sys

def factorial(argv):
	arg1 = int(sys.argv[1])
	if isinstance(arg1, int)==False:
		print("Error! Not an integer.")
		return
	fact=1
	for i in range(1, arg1+1):
		fact=fact*i
	print(fact)

factorial(sys.argv)