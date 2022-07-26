"""
Dilyana Koleva, July 2022
Intermediate Python Projects - Password Generator
A string of all available characters has been provided
The user must enter how many random passwords must be generated
and the length of the passwords
"""
import random

def create_pass():
    print("Password Generator")
    print("==================")
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
    number = input("How many passwords do you want to generate? ")
    number = int(number)
    length = input("How many characters should the password have? ")
    length = int(length)
    print("\nHere are your passwords: ")
    for pwd in range(number):
        passwords = ''
        for c in range(length):
            passwords += random.choice(chars)

        print(passwords)
        with open("passwords.txt", 'a') as f:
            f.write(passwords+ '\n')

if __name__ == '__main__':
    create_pass()