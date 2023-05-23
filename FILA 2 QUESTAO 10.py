numero = int(input("Digite um número de 1 a 6: "))

numeros_extenso = [
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis"
]

if numero >= 1 and numero <= 6:

    extenso = numeros_extenso[numero - 1]
    print("O número", numero, "por extenso é:", extenso)
else:
    print("Número invalidado Digite um número de 1 a 6.")