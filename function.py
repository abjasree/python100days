import random2
import hangman_words
import hangman_art
print(hangman_art.logo)
lives = 6
word = random2.choice(hangman_words.word_list).lower()

l=[]
for i in range(len(word)):
    l.append("_")
k = "".join(l)
print(k)
end_of_game = False
while end_of_game == False:
    guess = input("Guess a letter: ")
    count =0
    if guess in l:
        print("You have already guesses this number")
    for i in range(len(word)):
        if word[i] == guess:
            l[i] = guess
            print(f"Position of the guessed letter in the word: {i+1} :)")


    if guess not in word:
            lives -= 1
            print("Oops!!The letter you have guessed is not in the word!You lost a life!! ")
    print(hangman_art.stages[lives])
    k = "".join(l)
    print(k)

    if "_" not in k:
        end_of_game = True
        print("You Won!!!!")
    elif lives == 0:
        end_of_game = True
        print("You Lost!!!")
print(f"The correct word is {word}. :)")
