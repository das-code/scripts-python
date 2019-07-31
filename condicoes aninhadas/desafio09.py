valor = float(input("Valor do Produto: "))

print("Escolha a opção de pagamento")
print("1 > para a vista dinheiro ou cheque.")
print("2 > para a vista no cartao")
print("3 > para 2x no cartao")
print("4 > para 3x ou mais no cartao")

metodo = int(input("Informe sua escolha: "))

if metodo == 1:
    print(f"valor a pagar R${valor - (valor * 0.1)}")
elif metodo == 2:
    print(f"valor a pagar R${valor - (valor * 0.05)}")
elif metodo == 3:
    print(f"valor a pagar R${valor} em 2x de R${valor / 2}")
else:
    print(f"valor a pagar R${valor + (valor * 0.2)} dividido em 3 ou mais")
