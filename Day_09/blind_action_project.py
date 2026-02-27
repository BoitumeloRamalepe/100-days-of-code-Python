from art import logo

print(logo)
bidders_dictionary ={}

name = input("What is your name?: ")
bid_amount = int(input("What is your bid?: $ "))
bidders_dictionary[name] = bid_amount

next_bid = True
highest_bidder = ""
bid =0
while  next_bid:

    nextp =input("Are there any bidders? Type 'yes' or 'no'. \n").lower()
    
    if nextp == "yes":
        print("\n "* 100)
        name = input("What is your name?: ")
        bid_amount = int(input("What is your bid?: $ "))
        bidders_dictionary [name] = bid_amount
        
        for name in bidders_dictionary:
            if bidders_dictionary[name] > bid:
                bid = bidders_dictionary[name]
                highest_bidder = name

    else:
        next_bid =False
        print(f"The the winner is {highest_bidder} with a bid of ${bidders_dictionary[highest_bidder]}")
    
   
    

           