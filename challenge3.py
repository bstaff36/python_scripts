import sys

arg1=int(sys.argv[1])
arg2=int(sys.argv[2])
arg3=str(sys.argv[3])

if arg1!=arg2:
	print(max(arg1, arg2))
#if arg1==arg2:
#	pass   #if they are equal, do nothing
#elif arg1>arg2:    #if not equal, print the larger
#	print(arg1)
#else:
#	print(arg2)

if "time" in arg3:
	print(arg1+arg2)

if (arg1%2!=0 and arg2%2!=0) or (arg1%3==0 or arg2%3==0):
	print(arg3)

if len(sys.argv)>4:
	print("error")