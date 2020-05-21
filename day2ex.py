
def fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b 

def fizzbuzz():
	for i in range(101):
		if i % 15 == 0:
			print("fizzbuzz")
			i+=1
		elif i % 3 ==0:
			print("fizz")
			i+=1
		elif i % 5 == 0:
			print("buzz")
			i+=1
		else:
			print(i)
			i+=1

def fib_printer(x, y):
	fib_lst = []
	for i in range(x, y+1):
		fib_lst.append(fibonacci(i))
	seq = str(fib_lst[0])
	for num in range(1, len(fib_lst)):
		seq = seq + ", " + str(fib_lst[num])
	print(seq)

def thousand_fib_digits():
	thousand_fib_lst = []
	for i in range(10000):
		thousand_fib_lst.append(fibonacci(i))
	for x in range(len(thousand_fib_lst)):
		print(len(str(thousand_fib_lst[x])))


# thousand_fib_digits()
# fib_printer(0, 8)
# fizzbuzz()

