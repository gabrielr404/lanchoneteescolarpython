print(">>> MÁQUINA DE BEBIDAS <<<")
print("1 - Suco - R$ 5.00")
print("2 - Refrigerante - R$ 6.00")
print("3 - Água - R$ 3.00")
print("4 - Achocolatado - R$ 4.50")

codigo = int(input("Digite o código da bebida: "))

if codigo == 1:
    bebida = "Suco"
    preco = 5.00
elif codigo == 2:
    bebida = "Refrigerante"
    preco = 6.00
elif codigo == 3:
    bebida = "Água"
    preco = 3.00
elif codigo == 4:
    bebida = "Achocolatado"
    preco = 4.50
else:
    print("Código inválido!")
    exit()

print(f"\nVocê escolheu: {bebida}")
print(f"Preço: R$ {preco:.2f}")

pagamento = float(input("Digite o valor pago: R$ "))

if pagamento < preco:
    print("Valor insuficiente. Compra cancelada.")
else:
    troco = pagamento - preco
    print(f"Troco: R$ {troco:.2f}")
    print("Obrigado pela compra! Volte sempre!")