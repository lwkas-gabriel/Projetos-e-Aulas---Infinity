def media(lista):
    soma = 0
    for i in range(0, len(lista)):
        soma += lista[i]
    return soma/len(lista)

def populaDicionário():
    continua = "y"
    asteroideLog = {}

    while(continua == "y"):
        nomeAsteroide = input("Digite o nome do asteróide: ");
        listaDistancias = []

        for i in range (0,5):
            distancia = float(input("Inserir distância: "))
            listaDistancias.append(distancia);

        asteroideLog[nomeAsteroide] = listaDistancias;
        continua = input("Continuar? ")
    return asteroideLog


dicionario = populaDicionário();

for asteroide, vetorDistancias in dicionario.items():
  print(f"o {asteroide} está a uma distância média de {media(vetorDistancias)}")