import random

def somar(valor_1, valor_2):
    return valor_1 + valor_2

def compararValores(valor_1, valor_2):

    if valor_1 == valor_2:
        print(f"os valores {valor_1} e {valor_2} são iguais")
    elif valor_1 < valor_2:
        print(f"{valor_1} é menor que {valor_2}")
    else:
        print(f"{valor_2} é menor que {valor_1}")

def parOuImpar(valor):
    if valor == 0:
        print("nulo")
    elif valor % 2 == 0:
        print(f"{valor} é par")
    else:
        print(f"{valor} é impar")

def somaLimite (valorA, valorB, valorLimite):
    if valorA+valorB>valorLimite:
        return True
    else:
        return False

def comparaLimite (valorA, valorB, valorLimite):
    contaLimite = 0

    if valorA>valorLimite:
        contaLimite += 1
    
    if valorB>valorLimite:
        contaLimite += 1
    
    return contaLimite

def fizzBuzz (valor):
    if valor % 3 == 0 and valor % 5 == 0:
        return "FizzBuzz"
    elif valor % 3 == 0:
        return "fizz"
    elif valor % 5 == 0:
        return "buzz"
    else:
        return valor

def calculoPorcentagem(valor, porcentagem):
    valorAdicionado = valor;
    valorAdicionado += valor * (porcentagem/100)
    return valorAdicionado

def calculoArea(base, altura):
    area = (base * altura) / 2
    return area

def gerarNumeroAleatorio (limiteInferior, limiteSuperior):
    numero = random.randrange(limiteInferior, limiteSuperior, 1)
    return numero

def somaDadoUmNumero(limite):
    soma = 0
    for num in range(1, limite+1):
        soma += num
    return soma

def calculadora(numeroA, numeroB, operacao):
    if operacao == "+":
        return numeroA+numeroB

    if operacao == "-":
        return numeroA-numeroB

    if operacao == "*":
        return numeroA*numeroB

    if operacao == "/":
        return numeroA/numeroB

#prova

def calculandoSeculo(ano):
    seculo = int((ano/100) + 1)

    seculoRomano = ""

    while seculo != 0:
        if seculo >= 10:
            seculo -= 10
            seculoRomano += "X"
            continue
        elif seculo >= 9:
            seculo -= 9
            seculoRomano += "IX"
            continue
        elif seculo >= 5:
            seculo -= 5
            seculoRomano += "V"
            continue
        elif seculo >= 4:
            seculo -= 4
            seculoRomano += "IV"
            continue
        elif seculo >= 1:
            seculo -= 1
            seculoRomano += "I"
            continue

    return seculoRomano

print(calculandoSeculo(3899))