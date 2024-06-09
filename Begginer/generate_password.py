# IMPORT STRING AND RANDOM
import string
import random

# CREATE THE FUNCTION GENERATE PASSWORD WITH THE PARAMETER LENGHT
def generate_password(lenght):
    # CREATE A VARIABLE THAT WILL CONTAIN ALL THE CHARACTERS (LETTERS, NUMBERS AND SPECIAL CHARACTERS)
    characters = string.ascii_letters + string.digits + string.punctuation
    # CREATE A VARIABLE WHERE WILL SELECT RANDOMLY OF THE CHARACTERS VAR CHARACTERS
    # THEN WHE MAKE A FOR WITH THE _ PARAMETER (_ SAYS THAT THE FOR WILL BE REPEATED AS THE PROGRAM NEED) IN THE RANGE OF LENGHT PARAMETER
    password = "".join(random.choise(characters) for _ in range(lenght))
    # RETURN THE PASSWORD
    return password

# CREATE A VARIBLE THAT WILL BE A INPUT INSIDE A INT
lenght = int(input("Say the lenght of your password: "))

# CREATE A VARIABLE WHERE WE PUT THE GENERATE_PASSWORD FUNCTION
created_password = generate_password(lenght)

# PRINT THE FUNCTION VARIABLE
print(created_password)
