from art import logo

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', '1', 'h', 'i', 'j', 'k', 'l', 'm', '2', 'n', 'o', 'p', 'q', 'r', 's', 't', '3', 'u', 'v', 'w', '4', 'x', 'y', 'z', '5', ' ', '6', '!', '@', '#', '$', '%', '^', '&', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '7', 'O', 'P', 'Q', 'R', 'S', '8', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '*', '9', '(', ')', ',', '0', '.', '/', '?']

print(logo)
end = False
    def cipher(text, cipher_index, user_choice):
        message=""
        if user_choice == "decrypt":
            cipher_index = cipher_index*-1
        for letter in text:
            position = alphabet_list.index(letter)
            if position + cipher_index > len(alphabet_list)-1:
                new_position = position + cipher_index - len(alphabet_list)
            else:
                new_position = position + cipher_index
            message += alphabet_list[new_position]
        print(message)
while end is False:

    user_choice = input("What do you want to do? Encrypt or decrypt?")
    text = input("Write your message. \n")
    cipher_index = int(input("Chose a cipher key: \n"))

    def cipher(text, cipher_index, user_choice):
        message=""
        if user_choice == "decrypt":
            cipher_index = cipher_index*-1
        for letter in text:
            position = alphabet_list.index(letter)
            if position + cipher_index > len(alphabet_list)-1:
                new_position = position + cipher_index - len(alphabet_list)
            else:
                new_position = position + cipher_index
            message += alphabet_list[new_position]
        print(message)

    cipher(text, cipher_index, user_choice)

    continue_or_break = input("Do you wish to check again? Y/N\n")

    if continue_or_break == "Y":
        end = False
    elif continue_or_break =="N":
        end = True
    else: 
        print("Choose a valid option.")




