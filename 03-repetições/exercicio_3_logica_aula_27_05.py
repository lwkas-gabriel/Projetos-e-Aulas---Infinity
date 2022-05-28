numero = int(input("inserir numero inteiro e positivo: "))

if numero == 0:
    print(f"o numero {numero} eh zero")
elif numero % 2 == 0:
    print(f" o numero {numero} eh par")
else:
    print(f" o numero {numero} eh impar")
