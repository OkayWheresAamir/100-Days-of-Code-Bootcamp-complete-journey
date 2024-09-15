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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)

comp_choice = random.randint(0,2)
print("Computer chose :")
if comp_choice == 0:
    print(rock)
elif comp_choice == 1:
    print(paper)
elif comp_choice == 2:
    print(scissors)

if user_choice == comp_choice:
    print("Draw")
elif user_choice == 0:
    if comp_choice == 1:
        print("Lose")
    elif comp_choice == 2:
        print("Win")
elif user_choice == 1:
    if comp_choice == 2:
        print("Lose")
    elif comp_choice == 0:
        print("Win")
elif user_choice == 2:
    if comp_choice == 0:
        print("Lose")
    elif comp_choice == 1:
        print("Win")