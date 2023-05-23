distancia = float(input("qual a distância percorrida (em quilômetros): "))
combustivel = float(input("Qual a quantidade de combustível gasta (em litros): "))
consumo_medio = distancia / combustivel
gasto_combustivel = 4.50 * combustivel 
print(f"Consumo médio: {consumo_medio:.2f} km/l")
print(f"Gasto com combustível: R$ {gasto_combustivel:.2f}")