ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
ano_futuro = int(input("Digite o ano que você deseja saber qual seria a sua idade"))

idade_atual = ano_atual - ano_nascimento

idade_futura = ano_futuro - ano_nascimento
print("Idade atual:", idade_atual, "anos")
print("Idade em 2099:", idade_futura, "ano