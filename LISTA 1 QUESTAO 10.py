distancia = float(input("Digite a distância percorrida (em quilômetros): "))
combustivel = float(input("Digite a quantidade de combustível gasta (em litros): "))
consumo_medio = distancia / combustivel
gasto_combustiel = 4.50 * combustivel 

print(f"Consumo médio: {consumo_medio:.2f} km/l")
print(f"Gasto com combustível: R$ {gasto_combustivel:.2f}")