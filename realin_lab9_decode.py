#lab 9 - Realin is Decode

def decode():
    password_dec = int(input("Insert the password to decode: "))
    password_dec = list(password_dec)
    for each_char in range(password_dec):
        new = []
        each_char += 3
        new.append(each_char)
    new = str(new)
    return new


menu = print("""Menu
-------------
1. Encode
2. Decode
3. Quit""")

choice = int(input("Please enter an option: "))


while choice == True:
    if choice == 3:
        break
    elif choice == 2:
        print(decode())
    elif choice == 1:
        pass