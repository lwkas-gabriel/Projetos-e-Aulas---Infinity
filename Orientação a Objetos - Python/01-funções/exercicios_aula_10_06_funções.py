##Aquecimento da aula

"""valor = float(input("Digita salario: "))

novoSalario = valor

if valor <= 1000:
    novoSalario *= 1.15
elif (valor > 1000) and (valor <= 3000):
    novoSalario *= 1.1
elif valor > 3000:
    novoSalario *= 1.05

print(f"o seu novo salario eh ${novoSalario}")

somaIdades = 0
numero = 0

for i in range(0, 10):
    somaIdades += int(input("inserir idade: "))
    numero += 1

mediaIdades = somaIdades/numero

print(numero)

if mediaIdades < 18:
    print(f"só os jovi = média das idades eh {mediaIdades}")
elif mediaIdades >= 18 or mediaIdades < 58:
    print(f"bando de pagador de boletos = média das idades eh {mediaIdades}")
else:
    print(f"só boomer chato = média de idades eh {mediaIdades}")"""

## Exercicios da aula!

#1
def calcularMedia(num1, num2):
    media = (num1 + num2)/2
    print(f"a média dos numeros eh {media}")

#2
def verificar(num):
    if num == 0:
        print("nulo!")
    elif num < 0:
        print("negativo")
    else:
        print("positivo")

#3
def verificarVogais(palavra):
    contadorVogais = 0
    for caracter in palavra:
        if caracter.lower() in "aeiou":
            contadorVogais += 1
    print(f"você tem vogais {contadorVogais} na sua palavra")

#4
def verificaQuantosPares(num1, num2):
    if (num1 % 2 == 0) and (num2 % 2 == 0):
        return 2
    elif (num1 % 2 == 0) or (num2 % 2 == 0):
        return 1
    else:
        return 0

#5
def calculaPorcentagem(numero, porcentagem):
    return numero + (numero * porcentagem/100)

#6
def verificaPar():
    numero1 = int(input("inserir primeiro numero par: "))
    numero2 = int(input("inserir segundo numero par: "))
    if numero1 > numero2:
        return numero1
    else:
        return numero2


def verificaImpar():
    numero1 = int(input("inserir primeiro numero impar: "))
    numero2 = int(input("inserir segundo numero impar: "))
    if numero1 > numero2:
        return numero1
    else:
        return numero2

def mensagem(nome, msg="Saudações, "):
    print(f"{msg}{nome}")

#6
def saudacao(nome="fulaninho de tal"):
    print(f"olá, {nome}")

#7
def calculadora(num1, num2, op="+"):
    if op == "+":
        return num1+num2
    elif op == "-":
        return num1 - num2
    elif op == "/":
        return num1 / num2
    elif op == "*":
        return num1 * num2
    else:
        return "acho que voce fez bobagem, lucas"

#9
def contandoCaracteresFrase(frase):
    fraseSemEspaco = frase.replace(" ", "")
    return len(fraseSemEspaco)


#10
def somaAteN(numeroLimite):
    soma = 0
    for i in range(1, numeroLimite+1):
        soma += i

    return soma


print(contandoCaracteresFrase("essa eh uma frase teste"))
