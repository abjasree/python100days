import random2
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
images = [rock, paper, scissors]
print("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
value = int(input())
if (value >= 3) or (value <0):
    print("You typed an invalid number, you lose!")
else:
    print(images[value])
    print("Computer choose: ")
    value1 = random2.randint(0,2)
    print(images[value1])
    if value == value1:
         print("Draw!!")
    elif (value == 0 and value1 == 2) or (value == 1 and value1 == 0) or (value == 2 and value1 ==1):
        print("You win!!")
    else:
         print("You lose!!")
