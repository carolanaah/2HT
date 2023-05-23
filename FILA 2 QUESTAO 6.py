peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))
imc = peso / (altura ** 2)
print("Seu IMC é:", imc)

if imc < 18.5:
    print("Diagnóstico: abaixo do  peso")
elif imc < 25:
    print("Diagnóstico: Intervalo normal")
elif imc < 30:
    print("Diagnóstico: Sobrepeso")
elif imc < 35:
    print("Diagnóstico: Obesidade classe I")
elif imc < 40:
    print("Diagnóstico: Obesidade classe II")
else:
    print("Diagnóstico: Obesidade classe III")