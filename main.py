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
    ______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

a = int(input("What do you choose? Type 0 for Rock, 1 for Scissors and 2 for Paper? "))
lista=[rock, scissors, paper]
b=random.randint(0,2)
print(f'You choosed:\n{lista[a]}\nComputer choosed:\n{lista[b]}')
if a == b:
  print("Nobody wins, try again.")
if (a == 0 and b == 2) or (a == 1 and b == 0) or (a == 2 and b == 1):
  print("You lost")
if (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
  print("You won")
