#Who is going to pay
import random2
names = input("Give me everybody's names, seperated by a comma. ")
nameslt = names.split(", ")
chosen_name = random2.choice(nameslt)
print(f"The person who have to pay today is {chosen_name}")
