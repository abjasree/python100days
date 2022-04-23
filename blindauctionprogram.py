
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# HINT: You can call clear() to clear the output in the console.

print(logo)
auction_bid = {}
end = True
while end:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    auction_bid[name] = bid
    repeat = input("Are there any other bidders? Type 'yes' or 'no' ")
    if repeat.lower() == "yes":
        clear()
    else:
        end = False
n = []
m = []
for i in auction_bid:
    n.append(i)
    m.append(auction_bid[i])
tot = max(m)
num = m.index(tot)
name = n[num]
print(f"The winner is {name} with a bid of ${tot}.")

