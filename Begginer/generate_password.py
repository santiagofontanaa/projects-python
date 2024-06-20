# Import modules
import random
import string
    
# create_password function
def create_password(password_length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(int(password_length)))
        return password

if __name__ == "__main__":
    print("PASSWORD GENERATOR")
    while True:
        while True:
            print("What will be your password length?")
            password_length = input().
            if password_length.isdigit() and (int(password_length) > 0):
            else:
                print("You must write a valid number!")

        # create new password and print
        random_password = create_password(password_length)
        print("PASSWORD: " + random_password)

        # .strip() quit blank space | .lower() make the input lowercase
        nueva_contraseña = input("Want to create an new password? (yes/no) ").strip().lower()
        # if password is not equal to "yes" we will break loop
        if nueva_contraseña != "yes":
            break
