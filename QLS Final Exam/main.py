import smtplib
from email.mime.text import MIMEText
from getpass import getpass  # Secure password input

# QLS Exam

# ANSI color codes
RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"

user_wins = 0

print(BLUE + "***** Welcome to the Q-LS Series Certification Exam *****\n\n" + RESET)

user_name = input("What's your name?\n")

print("\nLet's start, " + GREEN + user_name + RESET + "\n")

while True:
    # Question 1 (Multiple Choice)
    while True:
        print(
            "\nQuestion 1. When it is necessary to store the Q-LS system for long periods of time, how often should the batteries be cycle charged?\n")
        print("A) 3 months")
        print("B) 6 months")
        print("C) 9 months")
        print("D) 12 months")

        answer = input("\nPlease enter your answer (A, B, C, or D): ").upper()

        if answer == "A":
            print(GREEN + "That's Correct!" + RESET)
            user_wins += 1
            break
        elif answer in ["B", "C", "D"]:
            print(RED + "I'm sorry, that's not correct" + RESET)
            break
        else:
            print(YELLOW + "Please enter a valid choice (A, B, C, or D)" + RESET)

    # Question 2 (Multiple Choice)
    while True:
        print(
            "\nQuestion 2. What should be done before connecting or disconnecting battery terminals?\n")
        print("A) Grease Rollers")
        print("B) Ensure BATT breaker is ON")
        print("C) Ensure BATT breaker is OFF")
        print("D) Check for Voltage with DMM")

        answer = input("\nPlease enter your answer (A, B, C, or D): ").upper()

        if answer == "C":
            print(GREEN + "That's Correct!" + RESET)
            user_wins += 1
            break
        elif answer in ["A", "B", "D"]:
            print(RED + "I'm sorry, that's not correct" + RESET)
            break
        else:
            print(YELLOW + "Please enter a valid choice (A, B, C, or D)" + RESET)

    # Game Summary
    print(BLUE + "You've completed the exam and scored " + str(user_wins) + "/2" + RESET)

    # Ask the user for their Microsoft work email and password
    sender_email = input("Enter your Microsoft work email address: ")
    password = getpass("Enter your email password (hidden): ")


    # Email sending function
    def send_email(user_name, user_wins, sender_email, password):
        receiver_email = sender_email  # You can also send to yourself or another address

        smtp_server = "smtp.office365.com"  # Microsoft's SMTP server
        smtp_port = 587  # For TLS encryption

        subject = f"QLS Series Certification Score for {user_name}"
        body = f"User: {user_name}\nScore: {user_wins}/2"

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
