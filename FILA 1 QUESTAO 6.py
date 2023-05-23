indice_de poluição = float(input("Digite o índice de poluição que está sendo medido: "))
if indice_poluicao >= 0.5:
    print("Todos os grupos devem paralisar suas atividades.")
elif indice_poluicao >= 0.4:
    print("Grupos 1 e 2 devem suspender suas atividades.")
elif indice_poluicao >= 0.3:
    print("Grupo 1 deve suspender suas atividades.")
else:
    print("Índice de poluição dentro do limite aceitável.")