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

print("Welcome to Rock Paper Scissors!")
zahl_user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
zahl_random = random.randint(0, 2)
bilder = [rock, paper, scissors]

if zahl_user not in [0, 1, 2]:
    print("You chose an invalid number. You loose!")
else:
    print("You chose: " + bilder[zahl_user])
    print("PC chose: " + bilder[zahl_random])
    if zahl_user == zahl_random:
        print("It's a draw")
    elif (zahl_user == 0 and zahl_random == 1) or (zahl_user == 1 and zahl_random == 2) or (zahl_user == 2 and zahl_random == 0):
        print("You loose. PC won. Better luck next time.")
    elif (zahl_user == 0 and zahl_random == 2) or (zahl_user == 1 and zahl_random == 0) or (zahl_user == 2 and zahl_random == 1):
        print("You won. PC lost. PC is sad now :'(")
