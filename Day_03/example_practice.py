# example 1
print("Welcome to the rollercoaster!")
height =int(input("What is your height in cm? \n"))
bill =0
if height >= 120:
    print("You can ride the rollercoaster ")
    age = int(input("Enter your age : \n"))

    if age <12 :
        print("Child tickets are $5.")
        bill = 5

    elif age <=18 :
        print("Youth tickets are $7.")
        bill = 7

    elif age>=45 and age <=55:
        print("Tickets are free")
        bill =0
        
    else :
        print("Adult tickets are $12.")
        bill = 12
        
    photos = input("Do you want a photo taken? Y or N. \n")

    if photos == "Y":
        bill += 3
    
    print(f"Your final bill is ${bill}")
    

else:
    print("Sorry you have to grow taller before you can ride.")

#odulo example
# number_to_check = int(input("What is the number to check?\n"))

# if number_to_check % 2 ==0:
#     print(f"The number {number_to_check} is even")
# else:
#     print(f"The number {number_to_check} is odd")
