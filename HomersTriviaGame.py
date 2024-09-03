# Homer's Trivia Game

# ANSI color codes
RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"

user_wins = 0

print(BLUE + "***** Hi!!! *****\n***** Welcome Homer's Trivia Game *****\n\n" + RESET)

user_name = input("What's your name?\n")

print("\nThanks for playing, " + GREEN + user_name + RESET + "!\n")

while True:
    # Question 1
    while True:
        try:
            answer = int(input("\nQuestion 1. When did the Roman Empire fall?\n"))

            if answer == 476:
                print(GREEN + "That's Correct!" + RESET)
                user_wins += 1
                break
            else:
                print(RED + "I'm sorry, that's not correct" + RESET)
                break
        except ValueError:
            print(YELLOW + "Please enter a numeric guess" + RESET)

    # Question 2
    while True:
        answer = input("\nQuestion 2. What is the two-letter symbol for the element Gold?\n")

        if answer.lower() == "au":
            print(GREEN + "That's Correct!" + RESET)
            user_wins += 1
            break
        else:
            print(RED + "I'm sorry, that's not correct" + RESET)
            break

    # Question 3
    while True:
        try:
            answer = int(input("\nQuestion 3. How many continents are there?\n"))

            if answer == 7:
                print(GREEN + "That's Correct!" + RESET)
                user_wins += 1
                break
            else:
                print(RED + "I'm sorry, that's not correct" + RESET)
                break
        except ValueError:
            print(YELLOW + "Please enter a numeric guess" + RESET)

    # Question 4
    while True:
        try:
            answer = int(input("\nQuestion 4. How many planets are in the Solar System?\n"))

            if answer == 8:
                print(GREEN + "That's Correct!" + RESET)
                user_wins += 1
                break
            else:
                print(RED + "I'm sorry, that's not correct" + RESET)
                break
        except ValueError:
            print(YELLOW + "Please enter a numeric guess" + RESET)

    # Question 5
    while True:
        answer = input("\nQuestion 5. Who wrote the play 'Romeo and Juliet'?\n")

        if answer.lower() == "shakespeare" or answer.lower() == "william shakespeare":
            print(GREEN + "That's Correct!" + RESET)
            user_wins += 1
            break
        else:
            print(RED + "I'm sorry, that's not correct" + RESET)
            break

    # Question 6
    while True:
        try:
            answer = int(input("\nQuestion 6. How many degrees are in a right angle?\n"))

            if answer == 90:
                print(GREEN + "That's Correct!" + RESET)
                user_wins += 1
                break
            else:
                print(RED + "I'm sorry, that's not correct" + RESET)
                break
        except ValueError:
            print(YELLOW + "Please enter a numeric guess" + RESET)

    # Question 7
    while True:
        answer = input("\nQuestion 7. What is the capital of France?\n")

        if answer.lower() == "paris":
            print(GREEN + "That's Correct!" + RESET)
            user_wins += 1
            break
        else:
            print(RED + "I'm sorry, that's not correct" + RESET)
            break

    # Question 8
    while True:
        try:
            answer = int(input("\nQuestion 8. In what year did the Titanic sink?\n"))

            if answer == 1912:
                print(GREEN + "That's Correct!" + RESET)
                user_wins += 1
                break
            else:
                print(RED + "I'm sorry, that's not correct" + RESET)
                break
        except ValueError:
            print(YELLOW + "Please enter a numeric guess" + RESET)

    # Question 9
    while True:
        answer = input("\nQuestion 9. What is the largest mammal in the world?\n")

        if answer.lower() == "blue whale":
            print(GREEN + "That's Correct!" + RESET)
            user_wins += 1
            break
        else:
            print(RED + "I'm sorry, that's not correct" + RESET)
            break

    # Question 10
    while True:
        try:
            answer = int(input("\nQuestion 10. How many bones are in the human body?\n"))

            if answer == 206:
                print(GREEN + "That's Correct!" + RESET)
                user_wins += 1
                break
            else:
                print(RED + "I'm sorry, that's not correct" + RESET)
                break
        except ValueError:
            print(YELLOW + "Please enter a numeric guess" + RESET)

    # Game Summary
    print(BLUE + "You've completed the game and scored " + str(user_wins) + "/10" + RESET)

    # Ask to play again
    answer = input("Play again? (yes/no)\n").lower()
    if answer == "yes" or answer == "y":
        user_wins = 0  # Reset score for the new game
    else:
        print("Thanks for playing!")
        break
