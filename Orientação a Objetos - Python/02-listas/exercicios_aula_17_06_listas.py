from datetime import date

## Aquecimento
'''def calcularIdade(dia, mes, ano):
    data_atual = date.today();
    anoRetorno = data_atual.year - ano;

    if data_atual.day > dia and data_atual.month > mes:
        return f"Você tem {anoRetorno} anos"
    elif data_atual.day < dia and data_atual.month > mes:
        return f"Você tem {anoRetorno} anos"

    return f"Você tem {anoRetorno-1} anos"



print(calcularIdade(12,11,1992))'''

'Inicio de Listas'

#pessoas = ["Andre", "Bianca", "Carlos", "Daniela"]
pessoas = []
idades = []

'''for i in range(0, len(pessoas)):
    print(pessoas[i]);'''

def leLista(lista, lista2=[]):
    print(lista)
    #print(lista2)

#3
def leListaAprimorado(lista, lista2):
    for index in range(len(lista)):
        print(f"{lista[index]} - Idade:{lista2[index]}")

#1 e 2
def preencheListaCom5():
    for index in range(0, 5):
        pessoaNova = input("Inserir nome: ");
        pessoas.append(pessoaNova);
        idadePessoa = int(input("Inserir idade: "));
        idades.append(idadePessoa);
    leListaAprimorado(pessoas, idades)

#4
def listagemDeAprovados():
    aprovados = []
    for i in range(0, 5):
        nome = input("Inserir nome do aluno: ");
        media = float(input("Inserir média final do aluno:"));
        if media >= 7:
            aprovados.append(nome);
    leLista(aprovados)


#5
def retiraPares():
    impares = []
    for i in range(0, 5):
        numero = int(input("Inserir numero: "));
        impares.append(numero)

    for numero in impares:
        if numero % 2 == 0:
            impares.remove(numero)

    leLista(impares);


### Dicionários

#7
def populaDicionario():
    nome = input("Inserir nome: ")
    idade = int(input("inserir idade: "))
    cpf = input("Inserir cpf: ")
    endereco = input("Inserir endereco: ")

    dict = {"nome": nome,"idade": idade , "cpf": cpf, "endereco": endereco}
    print(dict)

#8
def maioresPessoas():
    dict = {}
    maiores = []
    for i in range(0,5):
        nome = input("inserir nome: ")
        altura = float(input("inserir altura: "))
        dict[nome] = altura;

    for item in dict.keys():
        if dict[item] >= 1.8:
            maiores.append(item)

    print(maiores)

#9
def apenasPares():
    listaPares = []
    for i in range(0, 10):
        numero = int(input("inserir numero: "))
        if numero % 2 == 0:
            listaPares.append(numero)

    leLista(listaPares)

apenasPares()
