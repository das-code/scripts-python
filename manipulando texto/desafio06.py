input_nome = str(input('Informe seu nome completo: ')).strip()
nome = input_nome.split()


print(f'Primeiro nome: {nome[0]}')
print(f'Ultimo nome: {nome[len(nome) - 1]}')
