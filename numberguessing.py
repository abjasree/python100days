import random2

logo = """ ________  ___  ___  _______   ________   ________           ________   ___  ___  _____ ______   ________  _______   ________          ________  ________      
|\   ____\|\  \|\  \|\  ___ \ |\   ____\ |\   ____\         |\   ___  \|\  \|\  \|\   _ \  _   \|\   __  \|\  ___ \ |\   __  \        |\_____  \|\_____  \     
\ \  \___|\ \  \\\  \ \   __/|\ \  \___|_\ \  \___|_        \ \  \\ \  \ \  \\\  \ \  \\\__\ \  \ \  \|\ /\ \   __/|\ \  \|\  \       \|____|\  \|____|\  \    
 \ \  \  __\ \  \\\  \ \  \_|/_\ \_____  \\ \_____  \        \ \  \\ \  \ \  \\\  \ \  \\|__| \  \ \   __  \ \  \_|/_\ \   _  _\            \ \__\    \ \__\   
  \ \  \|\  \ \  \\\  \ \  \_|\ \|____|\  \\|____|\  \        \ \  \\ \  \ \  \\\  \ \  \    \ \  \ \  \|\  \ \  \_|\ \ \  \\  \|            \|__|     \|__|   
   \ \_______\ \_______\ \_______\____\_\  \ ____\_\  \        \ \__\\ \__\ \_______\ \__\    \ \__\ \_______\ \_______\ \__\\ _\                ___       ___ 
    \|_______|\|_______|\|_______|\_________\\_________\        \|__| \|__|\|_______|\|__|     \|__|\|_______|\|_______|\|__|\|__|              |\__\     |\__\
                                 \|_________\|_________|                                                                                        \|__|     \|__|
                                                                                                                                                              """


def clear():
    i = 0
    while i <= 20:
        print("\n")
        i += 1
TURNHARD = 5
TURNLOW = 10

def checknum(num):
    global number
    i = num
    while i > 0:
        print(f"You have {i} attempt remaining to guess the number")
        num = int(input("Make a guess: "))
        if num > number:
            print("Too high \nGuess again")
        elif num < number:
            print("Too Low \nGuess again")
        else:
            print(f"You got it!! The answer is {number}")
        i -= 1
    if i == 0 and num != number:
        print(f"You run out of guesses and you lost!! The number is {number}")





again = True
while again:
    print(logo)
    print(f"Welcome to Number Guessing game!!")
    number = random2.randint(1, 100)
    print("I am thinking a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level.lower() == 'easy':
        checknum(TURNLOW)
    else:
        checknum(TURNHARD)
    play_again = input("Do you want to play again? Type 'y' or 'n': ")
    if play_again.lower() == 'n':
        again = False
    else:
        clear()
