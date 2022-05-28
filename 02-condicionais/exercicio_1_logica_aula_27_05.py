numeroA = int(input("inserir primeiro numero: "))

numeroB = int(input("inserir segundo numero: "))

ope = str(input("inserir operação: "))

numeroC = 0

if ope == "+":
    numeroC = numeroA + numeroB
    print("sua soma eh ", numeroC)
elif ope == "-":
    numeroC = numeroA - numeroB
    print("sua subtração eh ", numeroC)
elif ope == "*":
    numeroC = numeroA * numeroB
    print("sua multiplicação eh ", numeroC)
elif ope == "/":
    numeroC = float(numeroA/numeroB)
    print("sua divisão eh ", numeroC)
else:
    print("entrada invalida")
