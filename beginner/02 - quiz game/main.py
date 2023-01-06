 qt = "In this game only can response Y for Yes and N for No"
        print(qt)
        # First Question / Primera Pregunta
        q1 = input("Was Python created in 1990?: ")
        # If [q1] is equal than "Y" / Si [q1] es igual a "Y"
        if q1 == "Y":
            print("CORRECT, You pass!")
            # Second Question / Segunda Pregunta
            q2 = input("Are Python logo two Elephant?: ")
            if q2 == "N":
                print("CORRECT, You pass!")
                q3t = "THIS IS THE LAST QUESTION!"
                print(q3t)
                # Third Question / Tercera Pregunta
                q3 = input("Who create Python?: ")
                if q3 == "Guido van Rossum":
                    print("CORRECT, YOU ARE A GENIUS!")
                    continue
                
                # VARIABLES OF THE NAME OF Guido Van Rossum / VARIABLES DEL NOMBRE DE GUIDO VAN ROSSUM
                elif q3 == "guido van rossum":
                    print("CORRECT, YOU ARE A GENIUS!")
                    continue

                elif q3 == "GUIDO VAN ROSSUM":
                    print("CORRECT, YOU ARE A GENIUS!")
                    continue

                elif q3 == "guido van rossum":
                    print("CORRECT, YOU ARE A GENIUS!")
                    continue
                
                # Else [q3]
                else:
                    print("You lose in the last one! :c")
                    continue
            
            # If [q2] is equal than "Y" / Si [q3] es igual a "Y"
            elif q2 == "Y":
                print("YOU WRONG!, REPEAT THE QUIZ!")
                continue
            # Else [q2]   
            else:
                print("THAT NOT A VALID RESPONSE!, REPEAT THE QUIZ!")
                continue
        
        # If [q1] is equal than "N" / Si [q1] es igual a "N"
        elif q1 == "N":
            print("YOU WRONG!, REPEAT THE QUIZ!")
            continue

        # Else [q1]
        else:
            print("THAT NOT A VALID RESPONSE!, REPEAT THE QUIZ!")
            continue
    # Print of [q1] / Print de [q1]
    print(q1)

    
    # If [uinput] is equal than "N" the While break and the quit() close the program / Si [uinput] es igual a "N" el While se rompe y quit() cierra el programa    
    if uinput == "N":
        break
quit()
