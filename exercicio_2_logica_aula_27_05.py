user = str(input("inserir login: ")).lower()
password = str(input("inserir senha: "))
contador = 0

while contador <= 3:
    if user == "admin" and password == "619":
        print("acesso liberado!")
        break
    else:
        contador += 1
        print("acesso bloqueado!")
        if contador == 2:
            print("cuidado! você só tem mais uma tentativa!");

        if contador == 3:
            print("você tentou muitas vezes! seu acesso foi bloqueado por segurança!")

    user = str(input("inserir login: ")).lower()
    password = str(input("inserir senha: "))
