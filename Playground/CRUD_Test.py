print("Hello! Welcome to The Game\n\n")

user_name = input("What is your name?\n")

print("\nThanks for choosing to play today, " + user_name + "\n")

answer = int(input("Question 1. When did the Roman Empire fall?\n"))

if answer == 476:
	print("That's Correct!")
else:
	print("I'm sorry, that's not correct")

thing = input()

answer = input("Question 2. What is the two letter symbol for the element Gold?\n")

if answer == "Au" or answer == "AU" or answer == "au":
	print("That's Correct!")
else:
	print("I'm sorry, that's not correct")

thing = input()