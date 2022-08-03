import random
from secrets import choice

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

draw = '''
    _____
---'   __)_
      (____)_____
       __________)
    (______)
---.__(___)
'''

#Write your code below this line 👇
choices = [rock,paper,scissors,draw]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))
computer = random.randint(0,2)
if player >= 2 or player < 0:
  print("You chose an invalid number")

else:
  print(f"\nYou chose:")
  print(choices[player])
  print(f"\nComputer chose:")
  print(choices[computer])
  if (computer == 0) and (player == 2):
    print("You lose!")
  elif (computer == 2) and (player == 0):
    print("You win!")
  elif computer < player:
    print("You win!")
  elif player < computer:
    print("You lose!")
  else:
    print("It's a draw.")
    print(choices[3])