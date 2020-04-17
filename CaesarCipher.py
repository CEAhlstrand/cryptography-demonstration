# A Caesar Cipher is a simple example of symmetric key encryption in which the shift amount serves as a key
# Julius Caesar used a shift of 3 (i.e. a->d, b->e, ...)
# Because values are shifted one at a time, it is what's known as a 'Stream Cipher'
# While not secure by today's standards, a Caesar Cipher could be used as a step in a more detailed encryption algorithm
# For an explanation of ASCII values, visit https://www.computerhope.com/jargon/a/ascii.htm


# Takes in a string to be encrypted as well as a shift amount
# Returns the encrypted string
def caesar_encrypt(str_to_enc, shift):
    encryption = ''
    for char in str_to_enc:
        if char == " ":  # Spaces do not get shifted
            encryption += " "
        elif char.islower():
            shifted_numerical = (ord(char) - (97 - shift)) % 26
            shifted_ascii = shifted_numerical + 97
            encryption += chr(shifted_ascii)  # Alternatively, encryption = chr(((ord(char) - (97 - shift)) % 26) + 97)
        else:
            encryption += chr(((ord(char) - (65 - shift)) % 26) + 65)
    return encryption


# Takes in a string to be decrypted as well as a shift amount
# Returns the decrypted string
def caesar_decrypt(str_to_dec, shift):
    decryption = ''
    for char in str_to_dec:
        if char == " ":  # Spaces do not get shifted
            decryption += " "
        elif char.islower():
            decryption += chr(((ord(char) - (97 + shift)) % 26) + 97)
        else:
            decryption += chr(((ord(char) - (65 + shift)) % 26) + 65)
    return decryption


# Allows user to encrypt and decrypt different strings using an interactive console prompt
def main():
    print("Welcome to a demonstration of a Caesar Cipher")
    print("Enter a string to be converted, a shift amount, and whether you want to encrypt or decrypt (e or d). "
          "Separate by spaces")
    print("For example, type 'e dog 3' to encrypt the word 'dog' with a shift of 3")
    print("Alternatively, type 'quit' to quit")

    while True:
        instruction = input("Your instruction:")
        steps = instruction.split()

        if instruction == "quit":
            break
        elif steps[0] == "e":
            print(steps[1], " -> ", caesar_encrypt(steps[1], int(steps[2])))
        elif steps[0] == "d":
            print(steps[1], " -> ", caesar_decrypt(steps[1], int(steps[2])))
        else:
            print("Error in input")


if __name__ == "__main__":
    main()
