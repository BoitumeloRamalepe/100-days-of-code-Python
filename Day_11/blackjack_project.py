from art import logo
import random


play1=True

while play1:

    choice1 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    cards =[11,2,3,4,5,6,7,8,9,10,10,10,10]

    if choice1 == 'y':
        print(logo)
        random_cards=[]
        current_score =0
        for i in range(2):
            card =  random.choice(cards)
            random_cards.append(card)
            current_score  += card

        computer_firstcard =  random.choice(cards)
        print(f"Your cards: {random_cards} , current score: {current_score}")
        print(f"Computer's first card: {computer_firstcard} ")

        continue_playing =True

        while continue_playing:
           
            choice2 = input("Type 'y' to get another card, type 'n' to pass:").lower()
            if choice2 == "y":
                another_card =card
                random_cards.append(another_card)
                current_score = current_score + another_card

                print(f"Your cards: {random_cards} , current score: {current_score}")
                print(f"Computer's first card: {computer_firstcard} ")
            else:
                continue_playing =False 
                play1 =False 

    else:
        play1 =False
