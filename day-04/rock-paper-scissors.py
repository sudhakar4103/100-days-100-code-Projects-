import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    ______________________________________________________
---'   ____)_______________________________________________)
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hands = [rock, paper, scissors]

print("Welcome to 'Rock', 'Paper', 'Scissors' game!")

user_choice = int(input("Put 1 for 'rock', 2 for 'paper', 3 for 'scissors': "))

# Convert 1,2,3 to 0,1,2 (list index)
user_index = user_choice - 1

# Validate input
if user_index < 0 or user_index > 2:
    print("Invalid choice! Please enter 1, 2, or 3.")
else:
    print("\nYou chose:")
    print(hands[user_index])

    computer_index = random.randint(0, 2)
    print("\nComputer chose:")
    print(hands[computer_index])

    # Winning logic
    if user_index == computer_index:
        print("It's a draw!")
    elif (user_index == 0 and computer_index == 2) or \
         (user_index == 1 and computer_index == 0) or \
         (user_index == 2 and computer_index == 1):
        print("You win! 🎉")
    else:
        print("Computer wins! 😢")
