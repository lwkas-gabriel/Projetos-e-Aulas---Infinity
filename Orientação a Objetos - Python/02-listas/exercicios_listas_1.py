def readList(lista):
    for i in range(0,len(lista)):
        print(f"imprimindo lista {lista[i]}");

def somaPrimeiroUltimo(lista1, lista2):
    # soma = lista1[0] + lista2[len(lista2-1)];
    return lista1[0] + lista2[len(lista2)-1];

def somaValoresLista(lista):
    soma = 0;
    for i in range(0, len(lista)):
        soma += lista[i];
    return soma;

def concatena(lista):
    return lista *2;

def somaTresUltimos(lista):
    listaFatiada = lista[len(lista)-3:len(lista)]
    return somaValoresLista(listaFatiada)

def recebeCincoValoresEprinta():
    lista = [];
    for i in range(0,5):
        valor = int(input("inserir numero: "))
        lista.append(valor);

    for i in range(0, len(lista)):
        print(f"o {i+1}º numero é {lista[i]}")

def media():
    lista = [];
    soma = 0
    for i in range(0,3):
        valor = int(input("inserir nota: "))
        lista.append(valor);

    for i in range(0, len(lista)):
        soma += lista[i] 

    return soma/len(lista)

def quantidadeConsoantes(lista):
    consoantes = 0;
    vogal = 0;

    for i in range(0,len(lista)):
        if lista[i] == 'a' or lista[i] == 'e' or lista[i] == 'i' or lista[i] == 'o' or lista[i] == 'u':
            vogal += 1;
        else:
            consoantes += 1;

    return consoantes

def verificaParOuImpar(lista):
    listaPar = []
    listaImpar = []

    for i in range(0,len(lista)):
        if lista[i] % 2 == 0:
            listaPar.append(lista[i])
        else:
            listaImpar.append(lista[i])
    
    print(f"lista inicial: {lista}")
    print(f"lista de pares: {listaPar}")
    print(f"lista de impares: {listaImpar}")

def verificaFinalBoss(lista):
    listaEntre1e9 = []
    listaMultiplo3e5 = []
    listaPares = []

    for i in range(0,len(lista)):
        if lista[i] == 1 or lista[i] == 2 or lista[i] == 3 or lista[i] == 4 or lista[i] == 5 or lista[i] == 6 or lista[i] == 7 or lista[i] == 8 or lista[i] == 9:
            listaEntre1e9.append(lista[i])
        if lista[i] % 3 == 0 and lista[i] % 5 == 0:
            listaMultiplo3e5.append(lista[i])
        if lista[i] % 2 == 0:
            listaPares.append(lista[i])
    
    print(f"lista dos numeros entre 1 e 9: {listaEntre1e9}")
    print(f"lista dos multiplos de 3 e 5 : {listaMultiplo3e5}")
    print(f"lista de pares: {listaPares}")

lista = [];
    
# for i in range(0,10):
#     caracter = input("inserir caracter: ");
#     lista.append(caracter);

# print(quantidadeConsoantes(lista));

# for i in range(0,20):
#     numero = int(input("inserir numero: "));
#     lista.append(numero);

# verificaParOuImpar(lista)


for i in range(0,20):
    numero = int(input("inserir numero: "));
    lista.append(numero);

verificaFinalBoss(lista)




#print(f" sua média é {media()}");

# append(algo) adiciona algo ao final da lista
# insert(i, algo) adiciona algo na posição especificada
# pop(i) tira algo na posição especificada, ou pop(), que retira algo na ultima posição da lista
#  del(lista[i:j]), faz o mesmo que pop, no entanto é passado um intervalo
    # começa mas não inclui o i e vai até j