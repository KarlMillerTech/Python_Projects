# imports
import random

# main code

# the following is user input
amountoftimes = input("How many passwords would you like generated? ") # number of passwords to be generated
pw_length = input("What's the length of characters in your password? ") # the number of total characters
lowercasetimes = input("Lowercase letters? ")
upcasetimes = input("Upper case? ")
numbertimes = input("Numbers? ")

# does calculations based on how many of each type of character you selected
lowercase = "abcdefghijklmnopqrstuvwxyz" * lowercasetimes
number = "0123456789" * numbertimes
upcase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * upcasetimes

# if/else statement to make strings
if (lowercasetimes == 0):
    alphabet = number + upcase
elif (numbertimes == 0):
    alphabet = upcase + lowercase
elif (upcasetimes == 0):
    alphabet = number + lowercase
else:
    alphabet = lowercase + number + upcase

# opens the file 'passwords.txt' for writing
file = open("passwords.txt","a")

# generates the passwords
for i in range(amountoftimes):
    mypw = ""
    for i in range(pw_length):
        next_index = random.randrange(len(alphabet))
        mypw = mypw + alphabet[next_index]

    file.write(mypw + '\n') # writes the password to the file

file.close() # closes the file
