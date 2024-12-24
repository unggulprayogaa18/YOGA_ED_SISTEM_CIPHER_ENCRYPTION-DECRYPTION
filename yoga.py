

def shift() -> int:
    while True:
        try:
            key = int(input("Enter shift (1-25): "))
            if key < 1 or key > 25:
                print("Please enter a value between 1 and 25")
            else:
                return key
        except ValueError:
            print("Enter an integer")

def encode():
    encoder = ""
    text = input("Enter text to encode: ")
    key = shift()

    for char in text:
        if char.isalpha(): #Only process alphabeth
            if char.islower(): #char is lowercase
                ascii = (ord(char) - ord('a') + key) % 26 + ord('a')
            elif char.isupper(): #char is uppercase
                ascii = (ord(char) - ord('A') + key) % 26 + ord('A')
            encoder += chr(ascii)

        else:
            encoder += char #Other character stay the same

    print(f"\033[92mEncoded text: {encoder}\033[0m")
    back()


def decode():
    decoder = ""
    cipher = input("\nEnter text to decode: ")
    key = shift()

    for char in cipher:
        if char.isalpha():
            if char.islower():
                ascii = (ord(char) - ord('a') - key) %26 + ord('a')
            elif char.isupper():
                ascii = (ord(char) - ord('A') - key) %26 + ord('A')
            decoder += chr(ascii)
        else:
            decoder += char #Other char stay the same
    
    print(f"\033[92mDecoded text: {decoder}\033[0m")
    back()
    
def back():
    #Back to main menu ?
    while True:
        choice = input("\nDo you want to return to the main menu? (y/n): ").lower()
        if choice == 'y':
            main() #Back to main menu
        elif choice == 'n':
            exit()
        else:
            print("Invalid choice. Please type 'y' for Yes or 'n' for No.")
    


def main():
    from welcome import up
    print(up)
    print("[1] Encrypt \n[2] Decrypt")

    user_input = input("Choose one of two options: ")
    
    match user_input:
        case "1":
            print("\n")
            encode()

        case "2":
            print("\n")
            decode()

        case _:
            print("\n [x] Invalid choice!. Please select 1 or 2.")
            main()

if __name__ == '__main__':
    main()
