texto = str(input('Digite uma frase: ')).lower().strip()

print(f'Letra A aparece: {texto.count("a")}')
print(f'Primeira letra A na posicao: {texto.find("a") + 1}')
print(f'Ultima letra A na posicao: {texto.rfind("a") + 1}')
