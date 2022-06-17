from Carro import Carro
from ContaBancaria import ContaBancaria


def listarClientes(lista):
    for cliente in lista:
        print("================");
        print(cliente.listarInformacoesDaConta());


# fusca = Carro("Chevrolet", "Fusca", 1995);

# fusca.ligar();
# fusca.acelera();
# fusca.acelera();
# fusca.acelera();
# fusca.acelera();
# fusca.acelera();
# fusca.acelera();
# fusca.acelera();
# fusca.verificaMarcha();
# print(f"{fusca.velocidadeAtual}");
listaClientes = [];

# for i in range(0, 3):
#     titular = input("Qual o titular da conta? ");
#     numero =  input("Qual o numero da conta? ");
#     saldo = float(input("Qual o saldo da conta? "));
#     escolheVip = input("Cliente vip? (S/N)");

#     if(escolheVip.lower() == "s"):
#         conta = ContaBancaria(titular,numero,saldo,True);
#         listaClientes.append(conta);
#     else:
#         conta = ContaBancaria(titular,numero,saldo);
#         listaClientes.append(conta);

# listarClientes(listaClientes);

conta1 = ContaBancaria("titular1","12355-56",5000);
conta2 = ContaBancaria("titular2","12356-56",1520);
conta3 = ContaBancaria("titular3","12357-56",45265, True);

listaClientes.append(conta1);
listaClientes.append(conta2);
listaClientes.append(conta3);

# conta1.depositar(500);
# conta1.checarSaldo();
# conta2 = ContaBancaria(titular,numero,saldo);

listarClientes(listaClientes);