# Dilsin Amirtharajah - Encoder
def password_encoder(password):
    encoded_password = ""

    for char in password:
        digit = int(char)

        shifted_digit = (digit + 3) % 10
        encoded_password += str(shifted_digit)

    return encoded_password


while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Quit")

    choice = input("Please enter an option: ")

    if choice == "1":
        password = input("Please enter your password to encode: ")
        encoded_password = password_encoder(password)
        print("Your password has been encoded and stored!")
        print()
    elif choice == "2":
        break
    else:
        print("Invalid option. Please try again.")
