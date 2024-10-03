import smtplib
import winsound
import os
import sys
from email.mime.text import MIMEText
from getpass import getpass  # Secure password input

# QLS Exam

# ANSI color codes
RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"

## Code to find the .wav files ##
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Define paths to the sound files
correct_wav_file_path = resource_path("resources/design study scenario complete.wav")
incorrect_wav_file_path = resource_path("resources/mesh failure.wav")

user_wins = 0

print(BLUE + "***** Welcome to the Q-LS Series Certification Exam *****\n\n" + RESET)

user_name = input("What's your name?\n")

print("\nLet's start, " + GREEN + user_name + RESET + "\n")




while True:


    # Question 1 (Multiple Choice)
    while True:
        print("\nQuestion 1. When it is necessary to store the Q-LS system for long periods of time, how often should the batteries be cycle charged?\n")
        print("A) 30 Days")
        print("B) 90 Days")
        print("C) 60 Days")
        print("D) 180 Days")

        answer = input("\nPlease enter your answer (A, B, C, or D): ").upper()

        if answer == "B":
            print(GREEN + "That's Correct!" + RESET)
            user_wins += 1
            winsound.PlaySound(correct_wav_file_path, winsound.SND_FILENAME)
            break
        elif answer in ["A", "C", "D"]:
            print(RED + "I'm sorry, that's not correct" + RESET)
            winsound.PlaySound(incorrect_wav_file_path, winsound.SND_FILENAME)
            break
        else:
            print(YELLOW + "Please enter a valid choice (A, B, C, or D)" + RESET)


    # Question 2 (Multiple Choice)
    while True:
        print("\nQuestion 2. What is the primary function of the Static Switch?\n")
        
        print("A) To switch the output state of the system ON and OFF")
        print("B) To transfer power between the Rectifier and the Inverter")
        print("C) To transfer output power source between the Reserve line and the Inverter")
        print("D) To switch the Q-LS system to Backup mode")

        answer = input("\nPlease enter your answer (A, B, C, or D): ").upper()

        if answer == "C":
            print(GREEN + "That's Correct!" + RESET)
            user_wins += 1
            winsound.PlaySound(correct_wav_file_path, winsound.SND_FILENAME)
            break
        elif answer in ["A", "B", "D"]:
            print(RED + "I'm sorry, that's not correct" + RESET)
            winsound.PlaySound(incorrect_wav_file_path, winsound.SND_FILENAME)
            break
        else:
            print(YELLOW + "Please enter a valid choice (A, B, C, or D)" + RESET)


    # Question 3 (Multiple Choice)
    while True:
        print("\nQuestion 3. What are the seven subsystems of the Q-LS?\n")
        
        print("A) Input, Rectifier, Inverter, Static Switch, Output, Logic & Housekeeping, Communications & HMI")
        print("B) Input, Rectifier, DC Rail, Inverter, Static Switch, Output, and Logic & Housekeeping")
        print("C) Static Switch, Ventilation fan system, Soft Start, Communications and HMI, Battery, Inverter, and Rectifier")
        print("D) Doc, Dopey, Bashful, Grumpy, Sneezy, Sleepy, and Happy")

        answer = input("\nPlease enter your answer (A, B, C, or D): ").upper()

        if answer == "B":
            print(GREEN + "That's Correct!" + RESET)
            user_wins += 1
            winsound.PlaySound(correct_wav_file_path, winsound.SND_FILENAME)
            break
        elif answer in ["A", "C", "D"]:
            print(RED + "I'm sorry, that's not correct" + RESET)
            winsound.PlaySound(incorrect_wav_file_path, winsound.SND_FILENAME)
            break
        else:
            print(YELLOW + "Please enter a valid choice (A, B, C, or D)" + RESET)




    # Exam Summary
    print(BLUE + "You've completed the exam and scored " + str(user_wins) + "/3" + RESET)

    # Ask the user for their Microsoft work email and password
    sender_email = input("Enter your Microsoft work email address: ")
    password = getpass("Enter your email password (hidden): ")

    # Email sending function
    def send_email(user_name, user_wins, sender_email, password):
        receiver_email = sender_email  # You can also send to yourself or another address

        smtp_server = "smtp.office365.com"  # Microsoft's SMTP server
        smtp_port = 587  # For TLS encryption

        subject = f"QLS Series Certification Score for {user_name}"
        body = f"User: {user_name}\nScore: {user_wins}/3"

        # Set up the MIME
        msg = MIMEText(body)
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Send email
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # Enable security (TLS encryption)
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Score email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")

    # Call the send_email function
    send_email(user_name, user_wins, sender_email, password)

    # Ask to try again
    answer = input("Try again? (yes/no)\n").lower()
    if answer == "yes" or answer == "y":
        user_wins = 0  # Reset score for the new game
    else:
        print("Thanks for completing the exam!")
        break
