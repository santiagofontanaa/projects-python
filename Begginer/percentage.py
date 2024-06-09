# We create the Money Input
money = input("Mencione el total de la cuenta: ")
# We create the Percentage Input
percentage = input("Ingresa el total de porcentaje: ")

# We calculate the percentage in the variable percentage_total
percentage_total = (int(money) / 100*int(percentage)) 

# Print in the CMD
print(percentage_total)
