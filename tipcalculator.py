print("Welcome to tip calculator")
totmoney = input("What was the total bill? $")
percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
num = input("How many people to split the bill? ")
sumtot = float(totmoney) + (float(totmoney)*int(percent))/100
oneperson = sumtot/int(num)
oneperson = "{:.2f}".format(oneperson)
print(f"Each person should pay: ${oneperson}")
