#1
def leTupla(tupla):
    print(tupla);

#2
def populandoTupla():
    lista = []
    for i in range(0,5):
        numero = input("Inserir numero: ");
        lista.append(numero);
    tupla = tuple(lista);
    leTupla(tupla);

#3
