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

choices= [rock, paper, scissors]

print("Welcome to the rock paper scissors game!")
player_choice = int(input("What do you choose? rock, paper, or scissors?..."
                      "type 0 for rock, 1 for paper, or 2 for scissors:\n"))

computer_choice = random.randint(0,2)

print("Player Choice:")
print(choices[player_choice])
print("Computer Choice:")
print(choices[computer_choice])

if player_choice == computer_choice:
    print("It's a tie!")

elif player_choice == 0 and computer_choice == 1:
    print("Oh No! You lost")
elif player_choice == 0 and computer_choice == 2:
    print("Yes! You won!!")

elif player_choice == 1 and computer_choice == 0:
    print("Yes! You won!!")
elif player_choice == 1 and computer_choice == 2:
    print("Oh No! You lost")

elif player_choice == 2 and computer_choice == 0:
    print("Oh No! You lost")
elif player_choice == 2 and computer_choice == 1:
    print("Yes! You won!!")
