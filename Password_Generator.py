import random
import string


def generate_password():
    length = int(input("How long do you want your password to be? "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for x in range(length):
        new_index = random.choice(characters)
        password += new_index
    return password

print(generate_password())