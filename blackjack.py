import random2

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def clear():
    i = 0
    while i < 15:
        print("\n")
        i += 1


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random2.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw!!"
    elif comp_score == 0:
        return "Lose, Opponent has Blackjack"
    elif user_score == 0:
        return "Win with Blackjack"
    elif user_score > 21:
        return "You went over. You lose!!"
    elif comp_score > 21:
        return "Opponent went over. You Win!!"
    elif user_score > comp_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    print(logo)
    user = []
    computer = []
    game_over = False
    for i in range(2):
        user.append(deal_card())
        computer.append(deal_card())
    while not game_over:
        user_score = calculate_score(user)
        comp_score = calculate_score(computer)
        print(f"Your cards: {user}, current score: {user_score}")
        print(f"Computer's first card: {computer[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            add_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if add_card == 'y':
                user.append(deal_card())
            else:
                game_over = True

    while comp_score != 0 and comp_score < 17:
        computer.append(deal_card())
        comp_score = calculate_score(computer)

    print(f"Your cards: {user}, current score: {user_score}")
    print(f"Computer cards: {computer}, computer score: {comp_score}")

    print(compare(user_score, comp_score))


while input("Do you want to play blackjack? Type 'y' for yes and 'n' for no: ") == 'y':
    clear()
    play_game()
