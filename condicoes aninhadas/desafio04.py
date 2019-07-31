idade = int(input("Qual e a sua idade? "))

if idade < 18:
    print(f"Ainda nao chegou a hora. Falta {18 - idade} anos")
elif idade == 18:
    print("Voce ja pode se alistar!")
else:
    print(f"Ja passou {idade - 18} anos do tempo para se alistar")
