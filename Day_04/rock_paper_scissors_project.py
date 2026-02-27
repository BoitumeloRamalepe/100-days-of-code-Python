import random

rock =('''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
       ''')

paper = '''
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
         '''

scissors ='''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images =[rock,paper,scissors]

person = int(input("What do you chooose?" \
            "Type 0 for rock, 1 for paper or 2 for scissors: \n"))

if 0<= person<=2:
    print(game_images[person])

    computer = random.randint(0,2)
    print(f"Computer chose:{computer} \n {game_images[computer]}")

    if person == computer:
        print("It's a Draw")

    elif person == 0 and computer == 1 :
        print("You lose!")

    elif person == 0 and computer == 2 :
        print("You win!")

    elif person == 1 and  computer == 0 :
        print("You win!")

    elif person == 2 and computer == 1 :
        print("You win!")

    elif person == 1 and computer == 2 :
        print("You lose!")
    
    elif person == 2 and computer == 0 :
        print("You lose!")
    


else:
   print("You typed an invalid number. You lose!")