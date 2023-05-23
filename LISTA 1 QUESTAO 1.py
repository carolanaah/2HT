not1 = float(input("Digite a primeira nota: "))
not2 = float(input("Digite a segunda nota: "))
not3 = float(input("Digite a terceira nota: "))
not4 = float(input("Digite a quarta nota: "))

media = (not1 + not2 + not3 + not4) / 4


if media < 4:
    situacao = "Em processo de Aprendizagem (Reprovou)"
elif media < 8:
    situacao = "Recuperação"
else:
    situacao = "passou de ano"