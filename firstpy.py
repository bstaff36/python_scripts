class Soldier:

	annual_raise =1.031
	num_of_ppl = 0

	def __init__(self, name, age, rank, pay):
		self.name = name
		self.age = age
		self.rank = rank
		self.pay = pay

		Soldier.num_of_ppl += 1

	def soldier_print(self):
		return "{} {}".format(self.rank.upper(), self.name)

	def set_raise(self):
		self.pay = self.pay*Soldier.annual_raise

	def print_pay(self):
		return "{0} {1} makes ${2:0,} a year.".format(self.rank.upper(), self.name, self.pay)

joe = Soldier("Stafford", 33, "WO1", 65000)
print(joe.soldier_print())
print(joe.print_pay())
print(joe.set_raise())
print(joe.print_pay())
print()

class BankAccount:

	def __init__(self, balance):
		self.balance = balance

	def deposit(self, m):
		self.balance += m

	def withdrawal(self, m):
		self.balance -= m

	def print_balance(self):
		return self.balance

user = BankAccount(500)
print(user.print_balance())
user.deposit(100)
print(user.print_balance())
user.withdrawal(200)
print(user.print_balance())

''' can create iterable classes with __iter__() method. def method in class and have it return self. Next define __next__() method for the class to be able to iterate. The __next__() method should contain logic describe how to iterate up using a counter and ending with "raise StopIteration" when value > end. Class __init__(self, start, end) should define start/stop values for iterables

