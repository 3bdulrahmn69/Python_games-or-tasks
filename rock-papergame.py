"""
This is a rock-paper game by me Abdulrahmn69
"""
import random

again = 'y'
while again == 'y':
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    user_action = input("Enter a choice (rock, paper, scissors): ")
    if user_action == computer_action:
        print(f"Computer choose {computer_action}")
        print("Draw")
    else:
        if (computer_action == "rock" and user_action == "scissors") \
            or (computer_action == "scissors" and user_action == "paper") \
            or (computer_action == "paper" and user_action == "rock"):
            print(f"Computer choose {computer_action}")
            print("U Lose")
        else:
            print(f"Computer choose {computer_action}")
            print("U Win")
    again = input("Again ? y / n:  ").strip().lower()