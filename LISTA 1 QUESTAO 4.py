peso_peixes = float(input("Digite o peso de peixes (em quilos): "))
excesso = max(0, peso_peixes - 50)
multa = excesso * 4.00
print("Excesso:", excesso)
print("Multa:", multa)