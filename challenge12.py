import sys

class Number:

	def __init__(self, n):
		self.n = n
		# print("Your number is: %s" %(self.n))

	def is_prime(self):
		for i in range(2, self.n):
			if self.n % i == 0:
				return False
				break
			else:
				if i == self.n-1:
					return True

	def get_divisors(self):
		lst=[]
		for i in range(1, self.n+1):
			if self.n % i == 0:
				lst.append(i)
		return lst

	def get_lcm(self, x):
		a = Number.get_gcd(self, x)
		return int((x*self.n)/a)

	def get_gcd(self, x):
		if self.n > x:
			small = x
		else:
			small = self.n
		for i in range(1, small+1):
			if((self.n % i == 0) and (x % i == 0)):
				gcd = i
		return gcd


arg1 = int(sys.argv[1])
arg2 = int(sys.argv[2])
n = Number(arg1)
a = n.is_prime()
print("Prime? %s" %(a))
a = n.get_divisors()
print("Factors: %s" %(a))
a = n.get_gcd(arg2)
print("GCD n and m: %s" %(a))
a = n.get_lcm(arg2)
print("LCM n and m: %s" %(a))