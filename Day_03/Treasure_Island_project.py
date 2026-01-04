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

direction = input("You are at a cross road .Where do you want to go? \n      Type 'LEFT' or 'RIGHT' ").upper()

if direction == "RIGHT":
    print("OOPS,You fell into a hole.\n Game Over. ")
elif direction == "LEFT":
    print("You've come to a lake. There is an island in the middle of the laake.")
    decision = input("      Type 'WAIT' to wait for an boat or Type 'SWIM' to swim across: ").upper()

    if decision == " SWIM":
        print("Attacked by shark.\n Game Over.")
    elif decision == "WAIT":
        print("You arrive at the island unharmed. There is a house with 3 doors.One red, one yellow, one blue. ")
        door = input("Which color do you choose?: ").upper()

        if door == "RED" :
            print("Burned by fire.\n Game Over.")
        elif door == "BLUE":
            print("Eaten by beasts.\n Game Over.")
        elif door== "YELLOW":
            print("You Win!")
        else:
            print("Game Over.")

else:
    print("You have entered an incorrect direction")       