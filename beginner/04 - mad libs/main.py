print("Welcome to Mad Libs!")

# Question for if the User want to play / Pregunta por si el Usuario quiere jugar
q = input("Do you want to play Mad Libs? Y/N")
# If [q] is equal than Y / Si [q] es igual a Y
if q == "Y":
    print("LETS PLAY!")
    # Input for the adjective 1 / Input para el adjetivo 1
    adj1 = input("Write an adjetive: ")
    # Input for the sustantivo 1 / Input para el sustantivo 1
    noun1 = input("Write an noun: ")
    # Input for the sustantivo 2 / Input para el sustantivo 2
    noun2 = input("Write an noun: ")
    # Text where the inputs replace with te adj or noun / Texto donde los inputs reemplazaran con el adjetivo o sustantivo
    text = f'Whether chipping away at a/an {adj1} statue or striching a patchwork {noun1}, crafting is always a labor of {noun2}.'
    print(text)
else:
    print("Good Bye!")
    quit()
print(q)
