nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5.0:
    print(f"REPROVADO! Media de {media :.2f}")
elif media >= 5.0 and media < 7:
    print(f"RECUPERAÇÃO! Media de {media :.2f}")
else:
    print(f"APROVADO! Media de {media :.2f}")
