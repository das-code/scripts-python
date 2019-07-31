from random import randint

print("1 > Perdra | 2 > Papel | 3 > Tesoura")

user = int(input("Escolha sua opção: "))
cpu = randint(0, 2)
escolhas = ["Pedra", "Papel", "Tesoura"]

print(
    f"\033[1;33mCPU\033[m > {escolhas[cpu]} vs {escolhas[user - 1]} < \033[1;31mVOCE\033[m"
)

if cpu == 0 and user == 2:
    print("Voce ganhou!")
elif cpu == 1 and user == 3:
    print("Voce ganhou!")
elif cpu == 2 and user == 1:
    print("voce Ganhou!")
elif cpu == 0 and user == 3:
    print("Voce perdeu!")
elif cpu == 1 and user == 1:
    print("Voce perdeu!")
elif cpu == 2 and user == 2:
    print("Voce perdeu!")
else:
    print("Empate!")
