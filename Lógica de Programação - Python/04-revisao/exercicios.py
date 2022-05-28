import random
import time

#1

"""numeroA = float(input("O seu primeiro número é: "))
numeroB = float(input("O seu segundo número é: "))

print(f"o 1º numero eh {numeroA} e o 2º numero eh {numeroB}")"""

#2

"""numero = float(input("Teste o numero: "))

if numero == 0:
    print("numero eh zero e zero eh nulo")
elif numero > 0:
    print(f"o numero {numero} eh positivo")
else:
    print(f"o numero {numero} eh negativo")"""

#3 

"""numeroSorteado = random.randint(1, 10)

guess = -1

while guess != numeroSorteado:
    guess = int(input("inserir palpite: "))
    if guess != numeroSorteado:
        print("erro! numero invalido")

print(f"parabens! o numero sorteado era {guess}")"""

#4
"""resposta = ""
contador = 0
contadorMorte = 0

    resposta = input("Telefonou para a vítima? (s/n)")
    if resposta == "s":
        contadorMorte += 1
    resposta = ""

    resposta = input("Esteve no local do crime? (s/n)")
    if resposta == "s":
        contadorMorte += 1
    resposta = ""

    resposta = input("Mora perto da vítima? (s/n)")
    if resposta == "s":
        contadorMorte += 1
    resposta = ""

    resposta = input("Devia para a vítima? (s/n)")
    if resposta == "s":
        contadorMorte += 1
    resposta = ""

    resposta = input("Já trabalhou com a vítima? (s/n)")
    if resposta == "s":
        contadorMorte += 1
    resposta = ""

if contadorMorte == 5:
    print("Assassino!")
elif contadorMorte == 3 or contadorMorte == 4:
    print("Cumplice")
elif contadorMorte == 2:
    print("Suspeito")
else:
    print("Inocente")"""


# repetições 

#1

"""numero = -1

while True:
    numero = int(input("inserir numero entre 0 e 10: "))
    if numero >= 0 and numero <= 10:
        print("entrada válida!")
        break
    print("numero invalido!")"""

#2


"""numeroMaior = 0
numero = 0

for num in range(1, 6):
    numero = float(input("inserir numero: "))
    if numero > numeroMaior:
        numeroMaior = numero

print(f"o maior numero eh {numeroMaior}");"""

#3

"""populacaoA = 80000
crescimentoA = 0.3

populacaoB = 200000
crescimentoB = 0.15

contador = 0

while populacaoB > populacaoA:
    contador += 1
    populacaoA += populacaoA * crescimentoA
    populacaoB += populacaoB * crescimentoB
    print(f"Após {contador} ano(s) população de A é igual a {populacaoA}")
    print(f"Após {contador} ano(s) população de B é igual a {populacaoB}")
    print("")
    time.sleep(1) #1 segundo = 1 ano

print(f"Em {contador} anos, a população de A superou a população de B")"""

#4 gerador tabuada

"""valorTabuada = int(input("Insira o multiplo da tabuada a ser gerada: "))

for num in range(1, 11):
    print(f"{valorTabuada} x {num} = {valorTabuada*num}")"""

#prova revisão

"""print("OLÁ, MUNDO!")

for num in range (1,2):
    print("OLÁ, MUNDO!")

contador = 0
while contador != 1:
    print("OLÁ, MUNDO!")
    contador += 1

mundo = "MUNDO"

if mundo == "MUNDO":
    print(f"OLÁ, {mundo}!")

hello = ""
while True:
    hello = input("Digite: ");
    if hello == "OLÁ, MUNDO!":
        print(hello)
        break"""