tabela_precos = { #dicionário
    "Verde": "R$ 10,00",
    "Azul": "R$ 20,00",
    "Amarelo": "R$ 30,00",
    "Vermelho": "R$ 40,00"
}
cor = input("Selecione a cor do jogo: ")
preco = tabela_precos.get(cor, "Cor inválida")
print("Preço:", preco)