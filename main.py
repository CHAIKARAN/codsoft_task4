rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
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

import random

game_images = [rock, paper, scissors]

while True:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. Press any other key to exit.\n"))

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number. Exiting the game.")
        break
    else:
        print("Your choice:")
        print(game_images[user_choice])

        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(game_images[computer_choice])

        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
            print("You win!")
        else:
            print("You lose!")

        play_again = input("Do you want to play another round? Type 'yes' or 'no': ").lower()
        if play_again != 'yes':
            print("Exiting the game.")
            break
