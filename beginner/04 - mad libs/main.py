print("Welcome to Mad Libs!")

q = input("Do you want to play Mad Libs? Y/N")
if q == "Y":
    print("LETS PLAY!")
    adj1 = input("Write an adjetive: ")
    noun1 = input("Write an noun: ")
    noun2 = input("Write an noun: ")
    text = f'Whether chipping away at a/an {adj1} statue or striching a patchwork {noun1}, crafting is always a labor of {noun2}.'
    print(text)
else:
    print("Good Bye!")
    quit()
print(q)
