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
choice = [rock, paper, scissors]
your_choice = int(input("Enter '0' for rock , '1' for paper and '2' for scissors \n "))
if your_choice > 2:
    print("Wrong choice !!")
else:

    print(f"You choose : "
          f"{choice[your_choice]}")

    num = random.randint(0, 2)
    print(f"Computer chooses : "
          f"{choice[num]}")
    if choice[your_choice] == choice[num]:
        print("It's a draw")
    elif your_choice == 0 and num == 1:
        print("You loose")
    elif your_choice == 0 and num == 2:
        print("You win")
    elif your_choice == 1 and num == 0:
        print("You loose")
    elif your_choice == 1 and num == 2:
        print("You loose")
    elif your_choice == 2 and num == 0:
        print("You loose")
    elif your_choice == 2 and num == 1:
        print("You win")
