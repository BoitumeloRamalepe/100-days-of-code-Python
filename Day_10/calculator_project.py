import art


def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1/n2


operations_dictionery = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide

}


#My solution before improvement

# num1 = float(input("What's your first number?: "))
# print("+\n" "- \n" "*\n" "/")

# result =0

# continuing =True
# result = num1
# while continuing:
    
#     sign= input("pick your operation: ")
#     num2 = float(input("Whats your second number?: "))
#     if sign == "*":
#        result= operations_dictionery["*"](result,num2)

#     elif sign == "+":
#         result= operations_dictionery["+"](result,num2)

#     elif sign == "-":
#         result= operations_dictionery["-"](result,num2)

#     elif sign == "/":
#         result= operations_dictionery["/"](result,num2)
        
#     else:
#         print("You have entered an invalid operation")
#         continuing = False

#     print(result)
#     proceed = input(f"Do you want to continue with the result {result} ,Type 'y' or 'n': ").lower()

#     if proceed == "y" :
#         continue
#     else :
#         continuing = False

   

def calculator():

    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))
    while should_accumulate:

        for symbol in operations_dictionery:
            print(symbol)

        sign = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        result = operations_dictionery[sign](num1, num2)
        print(f"{num1} {sign} {num2} = {result}")
        
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()
