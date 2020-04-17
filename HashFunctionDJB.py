# A hash function creates a fixed-length checksum(output) based on an input of any arbitrary length.
# In cryptography, this is used to verify that two values are equal.
# It is often used to verify the integrity of files, password verification, and digital signature verification.
# A good hash function meets the following criteria:
#       * Computationally Efficient
#       * Deterministic: the same input always results in the same output
#       * Collision Resistant: It is infeasible that any two given inputs result in the same checksum
#       * Pre-image Resistant: Given H(x), it is nearly impossible to determine x
#       * Avalanche Effect: A small change in the input results in a drastically different output
# Common examples include MD5, RIPEMD, and SHA

# This project uses the DJB hash function developed by Professor Daniel J. Bernstein to hash strings.
# This implementation (in Python 3) was converted from Prof. Bernstein's original function which can be found
# here: https://www.partow.net/programming/hashfunctions/#DJBHashFunction
# While not cryptographically sound due to frequent collisions, it is incredibly efficient and a simple example
# of a hash function. For example, both 'stylist' and 'subgenera' hash to the value '2945051873'
# For more info on collisions in DJB, check out
# https://softwareengineering.stackexchange.com/questions/49550/which-hashing-algorithm-is-best-for-uniqueness-and-speed


# Converts a string into its corresponding 32-bit hashed value
def djb(str_to_hash):
    hash_val = 5381  # 5381 is a 'magic constant' used to reduce collisions
    mask = 0xFFFFFFFF

    for char in str_to_hash:
        hash_val = (hash_val * 33) + ord(char)  # 33 is another 'magic constant'
        # Prof. Bernstein used the equivalent: hash_val = ((hash_val << 5) + hash_val) + ord(char)

    # The final hash_val requires a mask because Python tracks integers as a 32-bit signed integer
    # DJB was originally implemented to use 32-bit unsigned integers
    return hash_val & mask


def main():
    import time

    database = {
        "user1": "382886761",  # password1
        "carl37": "1089881053",  # dogLover123
        "notCarl73": "1834443867"  # catLover321
    }

    print("Suppose you have a database filled with users' login-s and hashed passwords:")
    print(database)

    time.sleep(7)
    print("\nBecause your database has hashed values, if a hacker managed to gain access to your database they would "
          "have no way of knowing what the users' passwords are")

    time.sleep(7)
    print("\nTo verify if a user has entered the correct password on a login attempt, you would need to check the "
          "hashed value of the user's input to the value in the database")

    time.sleep(7)
    print("\nFor example, if user 'carl137' entered 'password123' on a login attempt, they would be denied access")
    print("This is because 'password123' hashes to", djb("password123"), "which is not the appropriate value in the "
          "database -", database["carl37"])

    time.sleep(7)
    print("\nIf, on the other hand, user 'carl137' entered the password 'dogLover123', they would be allowed access "
          "because 'dogLover123' hashes to", djb("dogLover123"), "which matches the value stored in the database -",
          database["carl37"])


if __name__ == "__main__":
    main()
