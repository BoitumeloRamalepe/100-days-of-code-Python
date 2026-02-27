import random


# random_integer = random.randint(1,10) #this will produce a arandom whole number between 1 and 10 (inclusive)
# print(random_integer)

# random_number_0_to_1 = random.random()*10
# print(random_number_0_to_1)

# random_float = random.uniform(1,10)
# print(random_float)

#Task -print heads or tails
random_int=random.randint(0,1)

if random_int == 0:
    print("Heads")
else:
    print("Tails")