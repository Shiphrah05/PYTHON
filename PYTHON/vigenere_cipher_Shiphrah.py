def message():
    message = input("write a message... ")
    return message


# main program, this is going to return the message that the user inputs and print it out
message = message()
print(message)


def char_check(character):
    if character.isalpha() or character.isdigit():
        return True
    else:
        return False


def check_valid_key(key):
    for character in key:
        if char_check(character) == False:
            return False
    return True
# read more about


def write_key():
    while True:
        key = input("write a key (number or letter)... ")
        if check_valid_key(key) == True:
            return key
        else:
            print("invalid key, please try again")


# BODY
key = write_key()
print("This the key", key)
# 3
def encryption(text, key, shift):


position = 0
