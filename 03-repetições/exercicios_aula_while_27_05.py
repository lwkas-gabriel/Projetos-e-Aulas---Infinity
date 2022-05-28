import random

"""contador = 0

while contador <= 10:
    print(f"{contador}")
    contador += 1


contador = 100

while contador >= 0:
    print(f"{contador}")
    contador -= 1

contador = 50

while contador >= 10:
    print(f"{contador}")
    contador -= 1 """

"""contador = 70

while contador <= 94:
    print(f"{contador}")
    contador += 1"""

"""contador = 0

while contador <= 100:
    if contador == 0:
        print(f"o numero {contador} eh nulo")
    elif contador % 2 == 0:
        print(f"o numero {contador} eh par")
    contador += 1

contador = 0

while contador <= 100:
    if contador % 2 != 0:
        print(f"o numero {contador} eh impar")
    contador += 1

contador = 1
contadorPar = 0
contadorImpar = 0

while contador <= 10:
    numero = int(input(f"Digite o {contador}º numero: "))
    if numero == 0:
        print("zero eh zero")
        contador -= 1
    elif numero % 2 == 0:
        #print(f"o numero {numero} é par")
        contadorPar += 1
    else:
        #print(f"o numero {numero} é impar")
        contadorImpar += 1
    contador += 1


print(f"Voce digitou {contadorPar} numeros pares")
print(f"Voce digitou {contadorImpar} numeros impares")

condicaoParada = int(input("Insira a condição de parada: "))
contador = 0

while condicaoParada >= contador:
    print(contador)
    contador += 1"""

"""while True:
    nota = float(input("inserir nota de 0 a 10: "))
    if (nota >= 0) and (nota <= 10):
        print("nota válida")
        break
    else:
        print("nota inválida!")"""

#numeroSecreto = 6

numeroSecreto = random.randint(1,10)
guess = 0

while True:
    guess = int(input("inserir palpite (1 a 10): "))
    if numeroSecreto > guess:
        print("erro! numero secreto é maior que o palpite")
        continue
    elif numeroSecreto < guess:
        print("erro! numero secreto é menor que o palpite")
        continue
    else:
        print("parabéns, você acertou! O numero secreto era ", numeroSecreto)
        break
