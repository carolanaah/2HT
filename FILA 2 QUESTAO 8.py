numero = int(input("Digite um número de 1 a 7: "))

dias_semana = [
    "Domingo",
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado"
]


if numero >= 1 and numero <= 7:

    dia_semana = dias_semana[numero - 1]
    print("O dia da semana correspondente ao número", numero, "é:", dia_semana)
else:
    print("Número invalidado Digite um número de 1 e 7.")