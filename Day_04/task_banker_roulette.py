import random

#Figure out how to pick a random name from the list of friends.

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#Option 1
print(random.choice(friends))

#option 2
random_index = random.randint(0,4)
print(friends[random_index])



