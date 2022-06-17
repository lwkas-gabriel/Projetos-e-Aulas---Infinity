class ContaBancaria:
    def __init__(self, titular, numeroConta, saldo, vip="false" ):
        self.titular = titular;
        self.numeroConta = numeroConta;
        self.saldo = saldo;
        self.isVip = vip;

    def saque(self, valor):
        if self.saldo < valor:
            return "Inválido! Seu saldo é menor que a quantia inserida!";
        else:
            self.saldo -= valor;
            return "Sacando", valor, ":","Seu saldo agora é",self.saldo
    
    def depositar(self, valor):
        if valor < 0:
            return "Entrada inválida!"
        else:
            self.saldo += valor;
            return "Depositando",valor, ":","Seu saldo agora é",self.saldo

    def listarInformacoesDaConta(self):
        stringDoVip = "";
        if self.isVip == True:
            stringDoVip = "cliente vip!"
        else:
            stringDoVip = "cliente não vip!"


        return f"Olá, {self.titular} \n O numero da conta é {self.numeroConta} \n O saldo da conta é {self.saldo} \n VIP: {stringDoVip}"
