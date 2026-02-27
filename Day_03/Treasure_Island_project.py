print('''
      *******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')

print("Welcome to Treasure island.")
print("Your mission is to find the treasure")

choice1 = input("You are at a cross road ,where do you want to go?"  \
                "Type 'LEFT' or 'RIGHT' \n ").upper()

if choice1 == "LEFT":
    choice2 = input("You've come to a lake." \
    " There is an island in the middle of the lake." 
    " Type 'WAIT' to wait for an boat."
    " or Type 'SWIM' to swim across. \n ").upper()

    if choice2 == "WAIT":
        choice3 = input("You arrive at the island unharmed." \
        " There is a house with 3 doors." \
        "One red, one yellow, one blue." \
        " Which color do you choose? \n ").upper()

        if choice3 == "RED" :
            print("It's a room full of fire. Game Over")
        elif choice3 == "BLUE":
            print("You enter a room of beasts. Game Over.")
        elif choice3 == "YELLOW":
            print("You found the treasure. You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by a shark.\n Game Over.")
else:
     print("OOPS,You fell into a hole.\n Game Over. ")       