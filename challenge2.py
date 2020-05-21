import sys
arg1=int(sys.argv[1])
arg2=int(sys.argv[2])
arg3=float(sys.argv[3])
print(str(arg1+arg2)+" "+str(arg1*arg3)+" "+str(arg1%arg2)+" "+str(arg3//arg1))
arg11=arg1+1
arg22=arg2+1
arg33=arg3+1
print(str(arg11>>3)+" "+str(arg22/2)+" "+str(arg1 | arg2))
print(arg11+len(sys.argv)-1)