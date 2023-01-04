import random

# Var where the wins of the User and the Computer will be saved / Var donde las victorias del Usuario y la Computadora serán guardadas
uwin = 0
cwin = 0

# Options that the User and Computer can choose / Opciones que el Usuario y Computadora pueden elegir
options = ["rock", "paper", "scissors"]
options[0]

while True:
    # Input where the user can choose Rock, Paper, Scissors or leave the game / Input donde el usuario podrá elegir Piedra, Papel, Tijeras o dejar el juego.
    uinput = input("Welcome to RPS Game!, Pls select ROCK/PAPER/SCISSORS or X for Exit Game: ").lower()
    print(uinput)
    
    # If the User pick x the While will break
    if uinput == "x":
      break

    # If the User doesn't choise any from [options] the program will create a loop / Si el Usuario no selecciona nada de [options] el programa creará un loop
    if uinput not in options:
      continue
    
    # The Computer will select a number from 0, 1 or 2 / La Computadora seleccioan un numero desde 0, 1, 2
    cchoise = random.randint(0, 2)
    # The Computer search the number in options and transform the number to the list / La Computadora busca el numero en opciones y transforma el numero en la lista
    cpick = options[cchoise]
    print('Computer picked:', cpick)

    # If User select Rock and Computer pick Scissors the User Win and the program add 1 point to User / Si el Usuario selecciona Piedra y la Computadora Tijera el Usuario gana y el programa le suma 1 punto a Usuario
    if uinput == "rock" and cpick == "scissors":
        print("You win!")
        uwin += 1
    # If User select Ppael and Computer pick Piedra the User Win and the program add 1 point to User / Si el Usuario selecciona Papel y la Computadora Piedra el Usuario gana y el programa le suma 1 punto a Usuario
    elif uinput == "paper" and cpick == "rock":
        print("You win!")
        uwin += 1
    # If User select Scissors and Computer pick Paper the User Win and the program add 1 point to User / Si el Usuario selecciona Tijera y la Computadora Papel el Usuario gana y el programa le suma 1 punto a Usuario
    elif uinput == "scissors" and cpick == "paper":
        print("You win!")
        uwin += 1
    # If User select Rock and Computer pick Rock the User Tie / Si el Usuario selecciona Piedra y la Computadora Piedra Tijera el Usuario empata
    elif uinput == "rock" and cpick == "rock":
        print("You tie!")
    # If User select Paper and Computer pick Paper the User Tie / Si el Usuario selecciona Papel y la Computadora Papel Tijera el Usuario empata
    elif uinput == "paper" and cpick == "paper":
        print("You tie!")
    # If User select Scissors and Computer pick Scissors the User Tie / Si el Usuario selecciona Tijera y la Computadora Piedra Tijera el Usuario empata
    elif uinput == "scissors" and cpick == "scissors":
        print("You tie!")
    # The Computer wins the user and the program will add 1 point to Computer / La Computadora gana al usuario y el programa le agregará 1 punto a la Computadora
    else:
        print("You lose!")
        cwin += 1

# When the While break (the user type "x") the program print the results of the wins of User and Computer / Cuando el While se rompe (el usuario escribe "x") el programa hace un print con los resultados de las victorias del Usuario y la Computadora
print("Your wins: " + str(uwin) + " Machine wins: " + str(cwin))
# If UWIN (User Wins) is high than CWIN (Computer Wins) the program print that the user win / Si UWIN (Victorias de Usuario) es más alto que CWIN (Victorias de la Computadora) el programa hara un print diciendo que el usuari ganó
if uwin > cwin:
    print("You win the game!")
# If UWIN (User Wins) is equal than CWIN (Computer Wins) the program print that the user tie / Si UWIN (Victorias de Usuario) es igual que CWIN (Victorias de la Computadora) el programa hará un print diciendo que el usuari empató
elif uwin == cwin:
    print("You tie the game!")
# Else, if UWIN (User Wins) isn't higher or equal than CWIN (Computer Wins) the program print that the user lose / Si UWIN (Victorias de Usuario) no es mayor o igual a CWIN (Victorias de la Computadora) el programa hará un print diciendo que el usuario perdió
else: 
    print("You lose the game!")