# encryption 
def encryption(key, string):
    string = string.upper()
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for x in string:
        if x in letters:
            letter_index = (letters.find(x) + key) % len(letters)

            result = result + letters[letter_index]
        else:
            result = result + x
    return result

def decryption(key, string):
    string = string.upper()
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for x in string:
        if x in letters:
            letter_index = (letters.find(x) - key) % len(letters)

            result = result + letters[letter_index]
        else:
            result = result + x
    return result

def main_cypher():
    print("Hello welcome to Mridul's Ceaser Cypher!")
    while True:
        choice = input("\nDo you want to encrypt or decrypt? (type x to stop)").lower()
        if choice == "encrypt":
            string = input("What do you want to encrypt: ")
            rotation = int(input("Whats the rotation value: "))
            encrypted = encryption(rotation,string)
            print("here is your result: ",encrypted) #should print "ELOOB"
        elif choice == "decrypt":
            string = input("What do you want to decrypt: ")
            rotation = int(input("What's the rotation value: "))
            decrypted = decryption(rotation,string)
            print("here is your result: ",decrypted)
        elif choice == "x":
            break
        else:
            print("Error, please try again")

if __name__ == "__main__":
    main_cypher()