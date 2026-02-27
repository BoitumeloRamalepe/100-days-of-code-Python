from art import logo,vs
import random
from game_data import data


a = random.choice(data)
b = random.choice(data)

final_score =0
game_over = False

def compare_count(account_a,account_b, choice):

    if account_a == account_b:
        account_b = random.choice(data)
    
    if choice == "A" and account_a["follower_count"] > account_b["follower_count"]:
        account_a = account_b
        account_b=  random.choice(data)      
        return account_a,account_b,True

    elif choose == "B" and a["follower_count"] < account_b["follower_count"]:
        account_a = account_b
        account_b =  random.choice(data)
        return account_a,account_b,True
        
    else:
        return account_a,account_b,False


while not  game_over:
    print(logo)
    print(f"Compare A: {a["name"]}, a {a["description"]}, from {a['country']} ")
    print(vs)
    print(f"Against B: {b["name"]}, a {b["description"]}, from {b['country']} ")

    choose = input("Who has more followers? Type 'A' or 'B': ").upper()
    a,b, correct = compare_count(a,b,choose)

    if correct :
        final_score += 1
        print(f"You're right! Current score {final_score}")
    else:
        print("\n"*20 + logo )
        print(f"Sorry, that's wrong. Final score: {final_score}")
        game_over =True


# while not  game_over:
#     print(logo)
#     print(f"Compare A: {a["name"]}, a {a["description"]}, from {a['country']} ")
#     print(vs)
#     print(f"Compare B: {b["name"]}, a {b["description"]}, from {b['country']} ")

#     choose = input("Who has more followers? Type 'A' or 'B': ").upper()

   
#     if choose == "A" and a["follower_count"] > b["follower_count"]:
#         a = b
#         b = random.choice(data)      
#         final_score +=1
#     elif choose == "B" and a["follower_count"] < b["follower_count"]:
#         a = b
#         b =  random.choice(data)
#         final_score +=1
#     else:
#         print("\n"*20 + logo )
#         print(f"Sorry, that's wrong. Final score: {final_score}")
#         game_over =True