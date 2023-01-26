# Imports
import random

# Print :p
print('Welcome to Random Password Generator!')

# Input where U put if wan't to create an new account or not
q1 = input("Do you wan't to create a new password? Y/N: ")

# If q1 is equal than Y (yes)
if q1 == "Y" or "y": 
    # If U put Y as answer the program will make another question 
    q2 = input("Do you want your password with specials character? Y/N: ")
    # if q2 is equal than Y (yes)
    if q2 == "Y" or "y":
        # Here we ask to U how length the password will be
        pl = int(input("Enter the lenght of the password: "))
        # This is the characters that the program will use for the password
        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        # We see the quantity that U put in the input and create a grab random characters of s
        p = "".join(random.sample(s, pl ))
        print(p)
    #if q2 is equal than N (no)
    elif q2 == "N" or "n":
        # Here we ask to U how length the password will be
        pl2 = int(input("Enter the lenght of the password: "))
        # This is the characters that the program will use for the password
        s2 = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # We see the quantity that U put in the input and create a grab random characters of s
        p2 = "".join(random.sample(s2, pl2 ))
        print(p2)
# Else if q1 is equal than N (no)
elif q1 == "N" or "n":
    print('Oh :c')
    quit()
else:
    print("?")
