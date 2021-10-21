alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', '1', 'h', 'i', 'j', 'k', 'l', 'm', '2', 'n', 'o', 'p', 'q', 'r', 's', 't', '3', 'u', 'v', 'w', '4', 'x', 'y', 'z', '5', ' ', '6', '!', '@', '#', '$', '%', '^', '&', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '7', 'O', 'P', 'Q', 'R', 'S', '8', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '*', '9', '(', ')', ',', '0', '.', '/', '?']

user_choice = input("What do you want to do? Encrypt or decrypt?")
text = input("Write your message. \n")
cipher_index = int(input("Chose a cipher key: \n"))

def encrypt(text, cipher_index):
    encrypted=""
    for letter in text:
        position = alphabet_list.index(letter)
        if position + cipher_index > len(alphabet_list)-1:
            new_position = position + cipher_index - len(alphabet_list)
        else:
            new_position = position + cipher_index
        new_letter = alphabet_list[new_position]
        encrypted += new_letter
    print(encrypted)


def decrypt(text, cipher_index):
    decrypted=""
    for letter in text:
        position = alphabet_list.index(letter)
        if position + cipher_index > len(alphabet_list)-1:
            new_position = position + cipher_index - len(alphabet_list)
        else:
            new_position = position - cipher_index
        new_letter = alphabet_list[new_position]
        decrypted += new_letter
    print(decrypted)

if user_choice == "encrypt":
    encrypt(text, cipher_index)
elif user_choice == "decrypt":
    decrypt(text, cipher_index)
else:
    print("Please chose a correct option.")
