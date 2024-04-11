#lab 9 - Realin is Decode

def decode(password):
    # password = int(password)
    for each_char in (password):
        new = []
        each_char = int(each_char)
        each_char -= 3
        new.append(each_char)
    return new


menu = print("""Menu
-------------
1. Encode
2. Decode
3. Quit""")

choice = (input("Please enter an option: "))


while choice == "1" or choice == "2" or choice == "3":
    if choice == "2":
        password_dec = (input("Insert the password to decode: "))
        print(decode(password_dec))
    elif choice == "1":
        pass
    elif choice == "3":
        break