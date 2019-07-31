name = str(input("What's your name? ")).strip().title()

if name == "Gustavo":
    print("It's a pretty name!")
elif name == "Pedro" or name == "Maria" or name == "Paulo":
    print("Your name is very popular in Brazil!")
elif name in "Ana Claudia Jessica Juliana":
    print("Beautiful female name!")
else:
    print("Your name is very normal!")
print("Have a nice day, {}!".format(name))
