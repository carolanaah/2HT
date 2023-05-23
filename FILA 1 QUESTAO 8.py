num = int(input("Digite um num inteiro: "))
primo = True
if numero > 1:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break
else:
    primo = False

if primo:
    print(numero, "é primo.")
else:
    print(numero, "não é primo.")