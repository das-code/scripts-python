import math

angulo = float(input('Informe o angulo: '))
radiano = math.radians(angulo)

seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print(f'O angulo de {angulo} tem o SENO de {seno :.2f}')
print(f'O angulo de {angulo} tem o COSSENO de {cosseno :.2f}')
print(f'O angulo de {angulo} tem o TANGENTE de {tangente :.2f}')
