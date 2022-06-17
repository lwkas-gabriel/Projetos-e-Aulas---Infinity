class Carro:
    def __init__(self, marca, modelo, ano, automatico="false"):
        self.ligado = False;
        self.velocidadeAtual = 0;
        self.velocidadeMaxima = 120;
        self.marca = marca;
        self.modelo = modelo;
        self.ano = ano;
        self.automatico = automatico;

    def ligar(self):
        self.ligado = True;
        print("VRUM! VRUM!")

    def desliga(self):
        self.ligado = False;
        print("*Motor Parando*")

    def acelera(self):
        if self.ligado:
            if self.velocidadeAtual <= self.velocidadeMaxima:
                if self.velocidadeAtual == self.velocidadeMaxima:
                    print("Velocidade máxima atingida!")
                else:
                    self.velocidadeAtual += 20;
            else:
                print("Velocidade máxima atingida!")
        else:
            print("Carro desligado.")

    def verificaMarcha(self):
        if self.velocidadeAtual == 0 and self.velocidadeAtual < 20:
            print("1ª Marcha!");
        elif self.velocidadeAtual >= 20 and self.velocidadeAtual < 30:
            print("2ª Marcha!");
        elif self.velocidadeAtual >= 30 and self.velocidadeAtual < 45:
            print("3ª Marcha!");
        elif self.velocidadeAtual >= 45 and self.velocidadeAtual <= 60:
            print("4ª Marcha!");
        elif self.velocidadeAtual > 60:
            print("5ª Marcha!");
