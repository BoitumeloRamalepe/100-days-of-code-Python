from Day_08.art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(original_text ,shift_amount):
#     message = ""
#     position =  0
#     for letter in original_text:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             new_position = (position +shift_amount) % 26
#             new_position_letter = alphabet[new_position]
#         else:
#             continue    

#         message += new_position_letter
#     return message


# def decrypt(original_text,shift_amount):
#     message= encrypt(original_text,shift_amount)
#     decrypted_message = ""
#     for letter in message:
#         if letter in alphabet:
#             pos = alphabet.index(letter)
#             new_pos = (pos - shift_amount) % 26
#             new_pos_letter = alphabet[new_pos]
#         else:
#             continue
#         decrypted_message += new_pos_letter

#     print(decrypted_message)     



def caesar(original_text,shift_amount,encode_or_decode):

    message = ""

    if encode_or_decode=="decode":
        shift_amount *= -1

    elif encode_or_decode == "encode" :
        shift_amount *=1

    for letter in original_text:

        if letter not in alphabet:
            message +=letter
        else:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = (position + shift_amount) % 26
                new_position_letter = alphabet[new_position]
            
                message += new_position_letter
    print(f"Here is the {encode_or_decode}d result: {message}")

should_continue =True

print(logo)
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))  

    caesar(text,shift,direction)
    
    restart = input("Type 'yes' if you want to go again .otherwise type'no'.\n ").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")