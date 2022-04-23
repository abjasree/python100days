print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[abja]
*******************************************************************************''')
print("Welcome to the Treasure Island")
print("Your mission is to find the treasure!!")
direction = input("Which direction you want to go? left or right? ")
if direction.lower() != 'left':
    print("You fell into a hole. Game Over!!")
    print('''  ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#''')
else:
    swim = input("Do you want to swim or wait? ")
    if swim.lower() != 'wait':
        print("You are attacked by a trout. Game Over!!")
        print('''  ...
                     ;::::;
                   ;::::; :;
                 ;:::::'   :;
                ;:::::;     ;.
               ,:::::'       ;           OOO\
               ::::::;       ;          OOOOO\
               ;:::::;       ;         OOOOOOOO
              ,;::::::;     ;'         / OOOOOOO
            ;:::::::::`. ,,,;.        /  / DOOOOOO
          .';:::::::::::::::::;,     /  /     DOOOO
         ,::::::;::::::;;;;::::;,   /  /        DOOO
        ;`::::::`'::::::;;;::::: ,#/  /          DOOO
        :`:::::::`;::::::;;::: ;::#  /            DOOO
        ::`:::::::`;:::::::: ;::::# /              DOO
        `:`:::::::`;:::::: ;::::::#/               DOO
         :::`:::::::`;; ;:::::::::##                OO
         ::::`:::::::`;::::::::;:::#                OO
         `:::::`::::::::::::;'`:;::#                O
          `:::::`::::::::;' /  / `:#
           ::::::`:::::;'  /  /   `#''')
    else:
        door = input("Which door you want to open? red, yellow or blue? ")
        if door == 'red':
            print("You fell into fire and burned. Game Over!!")
            print('''  ...
                         ;::::;
                       ;::::; :;
                     ;:::::'   :;
                    ;:::::;     ;.
                   ,:::::'       ;           OOO\
                   ::::::;       ;          OOOOO\
                   ;:::::;       ;         OOOOOOOO
                  ,;::::::;     ;'         / OOOOOOO
                ;:::::::::`. ,,,;.        /  / DOOOOOO
              .';:::::::::::::::::;,     /  /     DOOOO
             ,::::::;::::::;;;;::::;,   /  /        DOOO
            ;`::::::`'::::::;;;::::: ,#/  /          DOOO
            :`:::::::`;::::::;;::: ;::#  /            DOOO
            ::`:::::::`;:::::::: ;::::# /              DOO
            `:`:::::::`;:::::: ;::::::#/               DOO
             :::`:::::::`;; ;:::::::::##                OO
             ::::`:::::::`;::::::::;:::#                OO
             `:::::`::::::::::::;'`:;::#                O
              `:::::`::::::::;' /  / `:#
               ::::::`:::::;'  /  /   `#''')
        elif door == 'blue':
            print("You are eaten by beasts. Game Over!!")
            print('''  ...
                         ;::::;
                       ;::::; :;
                     ;:::::'   :;
                    ;:::::;     ;.
                   ,:::::'       ;           OOO\
                   ::::::;       ;          OOOOO\
                   ;:::::;       ;         OOOOOOOO
                  ,;::::::;     ;'         / OOOOOOO
                ;:::::::::`. ,,,;.        /  / DOOOOOO
              .';:::::::::::::::::;,     /  /     DOOOO
             ,::::::;::::::;;;;::::;,   /  /        DOOO
            ;`::::::`'::::::;;;::::: ,#/  /          DOOO
            :`:::::::`;::::::;;::: ;::#  /            DOOO
            ::`:::::::`;:::::::: ;::::# /              DOO
            `:`:::::::`;:::::: ;::::::#/               DOO
             :::`:::::::`;; ;:::::::::##                OO
             ::::`:::::::`;::::::::;:::#                OO
             `:::::`::::::::::::;'`:;::#                O
              `:::::`::::::::;' /  / `:#
               ::::::`:::::;'  /  /   `#''')
        elif door == 'yellow':
            print("You win!!")
        else:
            print("Game over")
            print('''  ...
                         ;::::;
                       ;::::; :;
                     ;:::::'   :;
                    ;:::::;     ;.
                   ,:::::'       ;           OOO\
                   ::::::;       ;          OOOOO\
                   ;:::::;       ;         OOOOOOOO
                  ,;::::::;     ;'         / OOOOOOO
                ;:::::::::`. ,,,;.        /  / DOOOOOO
              .';:::::::::::::::::;,     /  /     DOOOO
             ,::::::;::::::;;;;::::;,   /  /        DOOO
            ;`::::::`'::::::;;;::::: ,#/  /          DOOO
            :`:::::::`;::::::;;::: ;::#  /            DOOO
            ::`:::::::`;:::::::: ;::::# /              DOO
            `:`:::::::`;:::::: ;::::::#/               DOO
             :::`:::::::`;; ;:::::::::##                OO
             ::::`:::::::`;::::::::;:::#                OO
             `:::::`::::::::::::;'`:;::#                O
              `:::::`::::::::;' /  / `:#
               ::::::`:::::;'  /  /   `#''')