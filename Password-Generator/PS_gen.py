# Import random library
import random

print ("Welcome to this very lean password generator!")


# The goals of the PS generator are:
# To give me a random string that will have a given number of characters (selected by user)
# At least 1 lower, 1 capitalized, 1 number and 1 symbol
# Give me multiple answers, so I have the ability to choose which one I like best


# Here we are storing all of the availalbe characters for generating a password
chars = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

# Here we want to know how many passwords to generate
# We add the INT() function in order to make sure the compile will have an integer
nr_passwords = input ("Let us know how many passwords you'd need: ")
nr_passwords = int(nr_passwords)

# Here we want to know how many characters the passwords should contain
# We add the INT() function in order to make sure the compile will have an integer
ps_length = input("Input the length you want your password to be: ")
ps_length = int(ps_length)


print('\nHere are your passwords: ')

for pwd in range(nr_passwords):
    passwords = ''
    for c in range(ps_length):
        passwords += random.choice(chars)
    print(passwords)