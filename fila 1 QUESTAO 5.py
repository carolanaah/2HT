codigo = int(input("Digite o código do operário: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
salario = horas_trabalhadas * 10.00
if horas_trabalhadas > 50:
    horas_excedentes = horas_trabalhadas - 50
    pagamento_excedente = horas_excedentes * 20.00
else:
    horas_excedentes = 0
    pagamento_excedente = 0