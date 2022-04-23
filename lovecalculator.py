print("Welcome to love calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

count1 = name1.lower().count('t')+name1.lower().count('r')+name1.lower().count('u')+name1.lower().count('e')+name2.lower().count('t')+name2.lower().count('r')+name2.lower().count('u')+name2.lower().count('e')
count2 = name1.lower().count('l')+name1.lower().count('o')+name1.lower().count('v')+name1.lower().count('e')+name2.lower().count('l')+name2.lower().count('o')+name2.lower().count('v')+name2.lower().count('e')
percent = str(count1)+str(count2)

if int(percent) < 10 or int(percent) > 90:
    print(f"Your score is {percent}, you go together like coke and mentos. ")
elif int(percent) <= 50 or int(percent) >= 40:
    print(f"Your score is {percent}, you are alright together. ")
else:
    print(f"Your score is {percent}. ")