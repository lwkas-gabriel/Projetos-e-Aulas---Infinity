#Aquecimento 1

'''class Carro:
    def __init__(self, modelo, ano, isAutomatico=False):
        self.modelo = modelo;
        self.ano = ano;
        self.velocidade = 0;
        self.isLigado = False;
        self.isAutomatico = isAutomatico;
        self.velocidadeMaxima = 120.0;

    def ligar(self):
        if self.isLigado == True:
            print("Carro já ligado...")
        else:
            print("*VRUM VRUM!!*")
            self.isLigado = True;

    def desligar(self):
        if self.isLigado == False:
            print("*carro já desligado*")
        else:
            print("*motor parando*")
            self.isLigado = False;
            self.velocidade = 0.0

    def acelara(self):
        if self.isLigado:
            if self.velocidade == self.velocidadeMaxima:
                print("você chegou na velocidade máxima")
            elif self.velocidade <= self.velocidadeMaxima:
                self.velocidade += 15;
            else:
                print("você chegou na velocidade máxima")
        else:
            print("ligue o carro antes..!")


    def get_marcha(self):
        if self.velocidade >= 0 and self.velocidade <= 20:
            print("1 marcha")
        elif self.velocidade > 20 and self.velocidade <= 30:
            print("2 marcha")
        elif self.velocidade > 30 and self.velocidade <= 35:
            print("3 marcha")
        elif self.velocidade > 35 and self.velocidade <= 45:
            print("4 marcha")
        elif self.velocidade > 45 and self.velocidade <= 55:
            print("5 marcha")
        else:
            print("6 marcha")


carro = Carro("Seila", 2022)
carro.ligar();
carro.acelara();
carro.acelara();
carro.acelara();
carro.get_marcha()

#Aquecimento 2

class Aluno:
    def __init__(self, matricula, nome):
        self.matricula = matricula;
        self.nome = nome;
        self.semestre = 1;
        self.media = 0.0;

    def calcularMedia(self):
        nota1 = float(input("Inserir primeira nota: "))
        nota2 = float(input("Inserir segunda nota: "))
        self.media = (nota1+nota2)/2

    def passouSemestre(self):
        if self.media >= 7:
            if self.semestre < 8:
                self.media = 0;
                self.semestre += 1;
            elif self.semestre == 8:
                print("parabens, você concluiu o curso!")
            else:
                self.media = 0;
                print("você concluiu o curso... vai fazer uma pós, sei lá '-' ")
        else:
            #self.media = 0;
            print("que pena... você não obteve nota suficiente para passar...")

    def logAluno(self):
        print(f"Olá, {self.nome}! Sua matricula é {self.matricula}, sua média atual é {self.media} e você está no {self.semestre}º semestre...")



aluno = Aluno("001", "Joãozinho")
aluno.calcularMedia();
aluno.passouSemestre();
aluno.calcularMedia();
aluno.passouSemestre();
aluno.calcularMedia();
aluno.passouSemestre();
aluno.logAluno();




class Pessoa:
    def __init__(self):
        self.__nome = "";
        self.__idade = 0;
        self.__cpf = "";

    @property
    def nome(self):
        return self.__nome;

    @nome.setter
    def nome(self, nome):
        self.__nome = nome;

    @property
    def idade(self):
        return self.__idade;

    @idade.setter
    def idade(self, idade):
        self.__idade = idade;

    @property
    def cpf(self):
        return self.__cpf;

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf;


pessoa = Pessoa();

nome = input("Inserir nome da pessoa: ");
idade = int(input("Inserir idade da pessoa: "));
cpf = input("Inserir cpf da pessoa: ");

pessoa.nome = nome;
pessoa.idade = idade;
pessoa.cpf = cpf;

print(f"Olá, {pessoa.nome}! Sua idade é {pessoa.idade} e o seu cpf é {pessoa.cpf}");


class Funcionario:
    def __init__(self, nome, salario, matricula, funcao):
        self.__nome = nome;
        self.__salario = salario;
        self.__matricula = matricula;
        self.__funcao = funcao;

    @property
    def salario(self):
        return self.__salario;

    @salario.setter
    def salario(self, valor):
        if valor > self.__salario * 1.2:
            print("valor alto demais...");
        elif valor < self.__salario or valor == self.__salario:
            print("valor menor ou igual ao salario atual");
        else:
            self.__salario = valor;


digitador = Funcionario("teste", 1000, "001", "Digitador");
digitador.salario = 1159;
print(digitador.salario) '''
