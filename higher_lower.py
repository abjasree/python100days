import random2

from game_art import logo
from game_art import vs
from game_data import data


def clear():
    i = 0
    while i <= 20:
        print("\n")
        i += 1


def compare(guess, dat1, dat2):
    if dat1['follower_count'] > dat2['follower_count']:
        return guess == 'A'
    else:
        return guess == 'B'


def game(data):
    num2 = random2.randint(0, len(data) - 1)
    end = True
    score = 0
    print(logo)
    while end == True:

        num1 = num2
        num2 = random2.randint(0, len(data) - 1)

        while num1 == num2:
            num2 = random2.randint(0, len(data) - 1)

        A = data[num1]
        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
        print(vs)
        B = data[num2]
        print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")
        pick = input("Who has more followers? Type 'A' or 'B': ").upper()
        is_correct = compare(pick, A, B)

        clear()
        print(logo)


        if is_correct:
            score += 1
            print(f"You are right!! Current Score: {score} ")
        else:
            end = False
            print(f"Sorry, that's wrong!! Final Score: {score} ")




game(data)
