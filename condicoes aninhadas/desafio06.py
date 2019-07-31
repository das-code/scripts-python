idade = int(input("Informe a sua idade: "))

print("De acordo com a sua idade voce e: ")

if idade <= 9:
    print("MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JUNIOR")
elif idade <= 20:
    print("SENIOR")
else:
    print("MASTER")
