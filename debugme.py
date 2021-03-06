'''This program has 2 logic errors in it.   Use the pdb program to step
through them and find them.
You can find a list of key commands explained at:
https://realpython.com/python-debugging-pdb/#essential-pdb-commands
You can also find a short tutorial at:
https://realpython.com/python-debugging-pdb/'''
import random

# import pdb
# pdb.set_trace()

def askplayer(prompt):
    theirchoice = ""
    while theirchoice in ['rock', 'paper', "scissors"]:
        theirchoice = raw_input(prompt)
    return theirchoice

# breakpoint()
def mychoice(choices):
    randomnumber = random.randint(1, 3)
    try:
        computerchoice = choices[randomnumber]
    except:
        pass
    return computerchoice

def compare(p1, p2):
    if p1 == p2:
        return 0
    if p1 == 'rock' and p2 == 'paper':
        return 2
    if p1 == 'rock' and p2 == 'scissors':
        return 1
    if p1 == 'paper' and p2 == 'rock':
        return 1
    if p1 == 'paper' and p2 == 'scissors':
        return 2
    if p1 == 'scissors' and p2 == "paper":
        return 1
    if p1 == 'scissors' and p2 == 'rock':
        return 2

choices = ["rock", "paper", "scissors"]

p = askplayer("Enter rock,paper or scissors:")
c = mychoice(choices)
print("I choose " + c)
if compare(p, c) == 0:
    print("its a Tie!")
if compare(p, c) == 1:
    print("You WIN!!")
if compare(p, c) == 2:
    print("You LOSE!!!")
