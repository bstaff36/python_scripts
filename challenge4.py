import sys

arg1=int(sys.argv[1])
sum=0
for i in range(1, arg1+1):
	if i%12==0:
		print(str(i//12)+" dozen")
	elif i%3==0:
		print("triangle")
	elif i%4==0:
		print("square")
	sum=sum+i
	i+=1
print(sum)