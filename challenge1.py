import sys
arg1=sys.argv[1]
arg2=sys.argv[2]
print(arg1+" "+arg2)
print(arg1[0]+arg2[2]+arg2[-1]+str(len(arg1)))
print("\n")
print(len(sys.argv)) #print total number of args including filename
print(arg1[1:4])
print("use of 'quotation marks'")
instr=input("please enter: ")
print(instr[1])