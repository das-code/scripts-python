from random import shuffle

primeiro = input('Nome do primeiro aluno: ')
segundo = input('Nome do segundo aluno: ')
terceiro = input('Nome do terceiro aluno: ')
quarto = input('Nome do quarto aluno: ')

alunos = [primeiro, segundo, terceiro, quarto]
shuffle(alunos)

print(f'O aluno escolhido foi {alunos}')
