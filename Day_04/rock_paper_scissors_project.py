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


person = int(input("What do you chooose?" \
            "Type 0 for rock, 1 for paper or 2 for scissors: \n"))


computer = random.randint(0,2)
#print(f"Computer chose: {computer}")

if person == 0 and computer == 1 :

    print(rock)
    print(f"Computer chose: {computer}\n {paper}")
    print("You lose!")

elif person == 0 and computer == 2 :
    print(rock)
    print(f"Computer chose: {computer}\n {scissors}")
    print("You win!")

elif person == 1 and  computer == 0 :
    print(paper)
    print(f"Computer chose: {computer}\n {rock}")
    print("You win!")

elif person == 1 and computer == 2 :
    print(paper)
    print(f"Computer chose: {computer}\n {scissors}")
    print("You lose!")
    
elif person == 2 and computer == 0 :
    print(scissors)
    print(f"Computer chose: {computer}\n {rock}")
    print("You lose!")
    
elif person == 2 and computer == 1 :
    print(scissors)
    print(f"Computer chose: {computer}\n {paper}")
    print("You win!")

else:
    print("Draw")