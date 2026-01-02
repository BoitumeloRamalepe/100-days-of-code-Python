print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how uch they need to pay based on their size choice.
#       > Small pizza(S):$15, Medium pizza(M):$20, Large pizza(L):$25


# todo: work out how much to add to their bill based on their pepperoni choice > +$2
#       > Add pepperoni for small pizza (Y or N): +$2
#       > Add pepperoni for medium or large pizza (Y or N): +$3

# todo: work out their final amoutnt based on whether if they want cheese  > +$3
#       > Add extra cheese for any size pizza (Y or N): +$1


# MY SOLUTION BELOW 
bill =0 
if  size == "S":
    bill += 15
    
    if pepperoni == "Y":
        bill += 2

elif size == "M":
    bill += 20

    if pepperoni == "Y":
        bill += 3

elif size == "L":
    bill += 25

    if pepperoni == "Y":
        bill += 3

else:
    print("You have chosen an invalid size.")

if extra_cheese == "Y":
    bill +=1

print (f"Your final bill is : ${bill}")


# Provided Solution

# todo: work out how much they need to pay based on their size choice.

# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("You have chosen an invalid size.")

# # todo: work out how much to add to their bill based on their pepperoni choice.
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# # todo: work out their final amount based on whether if they want extra cheese.
# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}.")