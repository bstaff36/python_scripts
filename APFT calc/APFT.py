import csv
from collections import defaultdict
import pprint

def main():
	m_pu = import_score_table("m_pu.csv")
	f_pu = import_score_table("f_pu.csv")
	su = import_score_table("su.csv")
	m_run = import_score_table("m_run.csv")
	f_run = import_score_table("f_run.csv")
	age_bracket = get_age()
	print("-"*10)
	print("-"*10)
	gender = get_gender()
	raw_pu = get_pu()
	raw_su = get_su()
	conv_run, raw_run = get_run()
	print("-"*10)
	print("-"*10)
	suscore = su_score(gender, raw_su, su, age_bracket)
	runscore = run_score(gender, conv_run, m_run, f_run, age_bracket)
	puscore = pu_score(gender, raw_pu, m_pu, f_pu, age_bracket)
	print("You did %s pushups for a score of %s." %(raw_pu, puscore))
	print("You did %s situps for a score of %s." %(raw_su, suscore))
	print("You ran your two-mile in %s for a score of %s." %(raw_run, runscore))
	print("-"*10)
	print("Your total score is %s." %(puscore+suscore+runscore))


def import_score_table(filename):
	input_file = csv.DictReader(open(filename, 'r'))
	csv_dict = {elem: [] for elem in input_file.fieldnames}
	for row in input_file:
		for key in csv_dict.keys():
			csv_dict[key].append(row[key])
	return csv_dict

def get_age():
	age_check = False
	while not age_check:
			try:
				age = int(input("Enter your age: "))
				if age > 0:
					age_check = True
				else:
					print("That's not a valid age! Try again. ")
			except ValueError:
				print("I'm sorry, you didn't enter an integer. Try again. ")
	if age <= 21:
		age_bracket=0
		print("You will be placed in the 17-21 y/o age bracket")
	if 22 <= age <= 26:
		age_bracket=1
		print("You will be placed in the 22-26 y/o age bracket")
	if 27 <= age <= 31:
		age_bracket=2
		print("You will be placed in the 27-31 y/o age bracket")
	if 32 <= age <= 36:
		age_bracket=3
		print("You will be placed in the 32-36 y/o age bracket")
	if 37 <= age <= 41:
		age_bracket=4
		print("You will be placed in the 37-41 y/o age bracket")
	if 42 <= age <= 46:
		age_bracket=5
		print("You will be placed in the 42-46 y/o age bracket")
	if 47 <= age <= 51:
		age_bracket=6
		print("You will be placed in the 47-51 y/o age bracket")
	if 52 <= age <= 56:
		age_bracket=7
		print("You will be placed in the 52-56 y/o age bracket")
	if 57 <= age <= 61:
		age_bracket=8
		print("You will be placed in the 57-61 y/o age bracket")
	if 62 <= age:
		age_bracket=9
		print("You will be placed in the over 62 y/o age bracket")
#	print(age)
	return age_bracket

def get_gender():
	gender = input("What is your gender? ").lower()
	while gender not in {"m", "f", "male", "female"}:
		print("You did not enter a valid gender. Please enter 'male' or 'female'.")
		gender = input("What is your gender? ").lower()
	gender = gender[0]
	return gender

# Gather APFT raw data, check for data entry errors, and store those values.  
def get_pu():
	rep_check = False
	while not rep_check:
			try:
				raw_pu = int(input("How many pushups did you do? "))
				if raw_pu >= 0:
					rep_check = True
				else:
					print("That's not a valid entry! Try again. ")
			except ValueError:
				print("I'm sorry, you didn't enter an integer. Try again. ")
	return raw_pu

def get_su():
	rep_check = False
	while not rep_check:
			try:
				raw_su = int(input("How many situps did you do? "))
				if raw_su >= 0:
					rep_check = True
				else:
					print("That's not a valid entry! Try again. ")
			except ValueError:
				print("I'm sorry, you didn't enter an integer. Try again. ")
	return raw_su

def get_run():
	rep_check = False
	while not rep_check:
			try:
				raw_run = input("What time (MM:SS) did you run your two-mile in? ")
				if len(raw_run) < 5:
					print("That's not a valid entry! Please use the format MM:SS. ")
				elif not raw_run[2] == ':':
					print("That's not a valid entry! Please use the format MM:SS. ")
				elif int(raw_run[0:2]) > 0 and raw_run[2] == ':' and int(raw_run[3:]) >=0:
					rep_check = True
				else:
					print("That's not a valid entry! Try again. ")
			except ValueError:
				print("I'm sorry, you didn't enter an integer. Try again. ")
	conv_run = int(raw_run[:2]+raw_run[3:5])
	return conv_run, raw_run

def pu_score(gender, raw_pu, m_pu, f_pu, age_bracket):
	if gender == "m":
		if raw_pu > 77:
			puscore = 100
			return puscore
		else:
			puscore = int(m_pu[str(raw_pu)][age_bracket])
			return puscore
	else:
		if raw_pu > 50:
			puscore = 100
			return puscore
		else:
			puscore = int(f_pu[str(raw_pu)][age_bracket])
			return puscore

def su_score(gender, raw_su, su, age_bracket):
	if raw_su < 21:
		suscore = 0
		return suscore
	if raw_su > 82:
		suscore = 100
		return suscore
	if gender == "m":
		suscore = int(su[str(raw_su)][age_bracket])
		return suscore
	else:
		pscore = int(su[str(raw_su)][age_bracket])
		return suscore

def run_score(gender, conv_run, m_run, f_run, age_bracket):
	if gender == "m":
		if conv_run <= 1300:
			runscore = 100
			return runscore
		else:
			run_check = False
			while not run_check:
				if str(conv_run) in m_run.keys():
					runscore = int(m_run[str(conv_run)][age_bracket])
					run_check = True
					return runscore
				else:
					conv_run+=1
	else:
		if conv_run <= 1531:
			runscore = 100
			return runscore
		else:
			run_check = False
			while not run_check:
				if str(conv_run) in f_run.keys():
					runscore = int(f_run[str(conv_run)][age_bracket])
					run_check = True
					return runscore
				else:
					conv_run+=1

if __name__== '__main__':
	main()

"""
ingest csv tables into dictionaries

5 dictionaires: m_pu, m_run, su, f_pu, f_run
Dictionaries take form of:
	{'key1':[value_1, value_2, value_3], 'key2': [value_a, ...]}
	where each value represents an age bracket from left to right:
	value 1 = 17-21
	value 2 = 22-26
	value 3 = 27-31
	value 4 = 32-36
	value 5 = 37-41
	value 6 = 42-46
	value 6 = 47-51
	value 8 = 52-56
	value 9 = 57-61
	value 10 = 62+

"""




