from os import closerange
import string

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', '1', 'h', 'i', 'j', 'k', 'l', 'm', '2', 'n', 'o', 'p', 'q', 'r', 's', 't', '3', 'u', 'v', 'w', '4', 'x', 'y', 'z', '5', ' ', '6', '!', '@', '#', '$', '%', '^', '&', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '7', 'O', 'P', 'Q', 'R', 'S', '8', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '*', '9', '(', ')', ',', '0', '.', '/', '?']

print("Welcome. You can encrypt or decrypt a message here. ")
user_choice = input("Encode or decode a message? ")
input_text = input("Write your message. ")
text = list(input_text)
cipher_value = int(input("Choose a cipher index. ")) #int(input("Choose an index: "))
#_________________________________________________________Defines what happens if cypher is larger than alphabet_list
def text_char_index(text):
    char_index_list = []
    for char in text:
        char_index = alphabet_list.index(char)
        char_index_list.append(char_index)
    return char_index_list
text_char_index = text_char_index(text)
#__________________________________________________Turns characters into numbers according to the alphabet_list
def in_numbers(user_choice, cipher_value): 
    encoded_list = []
    for char in text_char_index:
        if user_choice == "encode":
            if int(char) + cipher_value > len(alphabet_list) - 1:
                encoded_char = int(char) + cipher_value - (len(alphabet_list))
            else:
                encoded_char = int(char) + cipher_value
        elif user_choice == "decode":
            if int(char) + cipher_value > len(alphabet_list) - 1: 
                encoded_char = int(char) + cipher_value - (len(alphabet_list))
            else:
                encoded_char = int(char) - cipher_value
        else:
            print("Choose a correct operation. ")
        encoded_list.append(encoded_char)
    return encoded_list
in_numbers = in_numbers(user_choice, cipher_value)
#____________________________________________________________________Adds or removes cipher_value
def in_characters(in_numbers, alphabet_list):
    encoded_list = []
    for encoded_num in in_numbers:
        encoded_char = alphabet_list[encoded_num]
        encoded_list.append(encoded_char)
    return encoded_list
in_characters = in_characters(in_numbers, alphabet_list)
#__________________________________________________________Turns numbers into characters according to alphabet_list.
def message_to_string(in_characters):
    text_string = ''.join(in_characters)
    return text_string
text_string = message_to_string(in_characters)

print(f"The message is \n {text_string}")
