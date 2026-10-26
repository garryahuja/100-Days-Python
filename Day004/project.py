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

choose_one = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

if choose_one == 0:
    print(f"{rock}\nYou chose Rock")
elif choose_one == 1:
    print(f"{paper}\nYou chose Paper")
elif choose_one == 2:
    print(f"{scissors}\nYou chose Scissors")

option = [rock, paper, scissors]
random_option = random.randint(0,2)
if choose_one >= 3 or choose_one < 0:
    print("You provided an invalid option, you lose")
else:
    print(option[random_option])
    if option[random_option] == rock:
        print("Computer chose Rock")
    elif option[random_option] == paper:
        print("Computer chose Paper")
    elif option[random_option] == scissors:
        print("Computer chose Scissors")

if choose_one == 0 and random_option == 0:
    print("Its a draw")
elif choose_one == 0 and random_option == 1:
    print("You lose")
if choose_one == 0 and random_option == 2:
    print("You win")

if choose_one == 1 and random_option == 0:
    print("You win")
elif choose_one == 1 and random_option == 1:
    print("Its a draw")
elif choose_one == 1 and random_option == 2:
    print("You lose")

if choose_one == 2 and random_option == 0:
    print("You lose")
elif choose_one == 2 and random_option == 1:
    print("You win")
elif choose_one == 2 and random_option == 2:
    print("Its a draw")
