##Aquecimento 1

'''def isCPF(num):
    if len(num) == 11:
        return True
    else:
        return False

def buscaCPF(num, lista):
    teste = False

    if isCPF(num) == False:
        print("invalido")
    else:
        for cpfs in lista:
            if num == cpfs:
                teste = True

    return teste

pessoas = []
cpfs = []

teste = 0
while teste < 5:
    nome = input("inserir nome da pessoa: ")
    cpf = input("inserir cpf: ")

    if buscaCPF(cpf, cpfs) == False:
        pessoas.append(nome);
        cpfs.append(cpf)
        teste += 1
        print(teste)
    else:
        print("CPF já inserido")

print(pessoas)
print(cpfs)'''

##Aquecimento 2

'''def isCPF(num):
    if len(num) == 11:
        return True
    else:
        return False

def buscaCPF(num, dicionario):
    teste = False

    if isCPF(num) == False:
        print("cpf invalido")
    else:
        if dicionario.values() == num:
            teste = True

    return teste

def populaDicionario(dicionario):
    contador = 0
    while (contador < 2):
        nome = input("Digite o nome da pessoas: ");
        cpf = input("Inserir cpf: ")
        if buscaCPF(cpf, dicionario) == False:
                dicionario[nome] = cpf;
                contador += 1
        else:
                print("CPF já inserido")


dicionario = {}
populaDicionario(dicionario)
print(dicionario)'''

##Intro a Orientação a Objeto

##from  ContaCorrente import ContaCorrente se eu quiser em uma classe separada

class ContaCorrente:
    def __init__(self, favorecido, agencia, conta, saldo=0):
        self.agencia = agencia;
        self.conta = conta;
        self.favorecido = favorecido;
        self.saldo = saldo;

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return self.saldo
        else:
            print("valor negativo ou nulo... digite novamente!")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor;
        else:
            print("saldo insuficiente!");

    def transferir(self, destino, valor):
        if self == destino:
            print("conta de destino = origem... op invalida")
        else:
            if valor > self.saldo:
                print("saldo insuficiente")
            else:
                self.sacar(valor)
                destino.depositar(valor);

    def extrato(self):
        return f"Olá, {self.favorecido} \n" \
               f" O numero da conta é {self.conta} \n" \
               f" A sua " \
               f"agencia é {self.agencia} \n" \
               f" O seu saldo é R${self.saldo}"


'''favorecido = input("inserir nome: ")
agencia = input("inserir agencia: ")
conta = int(input("inserir conta: "))'''

'''conta1 = ContaCorrente("Lucas", "12345-2", "0001")
conta2 = ContaCorrente("Felipe", "12346-2", "0002")

conta1.depositar(500)
conta1.sacar(0)

conta2.depositar(400)
conta2.sacar(0)

conta1.transferir(conta2, 499)
conta1.extrato()

print(conta1.extrato())
print(conta2.extrato())'''


class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome;
        self.idade = idade;
        self.altura = altura;
        self.peso = peso;

    def engordar(self, valor):
        self.peso += valor

    def emagrecer(self, valor):
        self.peso -= valor

    def crescer(self, valor):
        self.altura += valor;

    def envelhecer(self):
        if self.idade <= 21:
            self.crescer(0.05)
            self.idade += 1
        else:
            print(f"você não cresce mais... pois você tem {self.idade} anos")
            self.idade += 1

    def fichaPessoal(self):
        return f"Olá, {self.nome} \n" \
               f" Você tem {self.idade} anos \n" \
               f" A sua altura é {self.altura:.2f} m \n" \
               f" Seu peso é {self.peso} kg"


teste = Pessoa("testolino", 12, 1.23, 40.5);
teste.envelhecer()
teste.envelhecer()
teste.envelhecer()
teste.crescer(0.1)
teste.envelhecer()
teste.engordar(10)
teste.engordar(3)
teste.engordar(5)
teste.engordar(5)
teste.engordar(15)
teste.envelhecer()
teste.envelhecer()
teste.envelhecer()
teste.envelhecer()
teste.envelhecer()
teste.envelhecer()
teste.envelhecer()
teste.envelhecer()
teste.envelhecer()
teste.emagrecer(8)
print(teste.fichaPessoal())
