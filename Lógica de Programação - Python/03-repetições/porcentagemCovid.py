contadorLeve = 0;
contadorSevero = 0;
contadorAssintomatico = 0;

for i in range(1, 11):
    print(f"{i}º paciente");
    print("0 - Assintomático");
    print("1 - Leve");
    print("2 - Severo");
    severidade = int(input("Inserir severidade: "));
    if(severidade ==0):
        contadorAssintomatico += 1;
    if(severidade ==1):
        contadorLeve += 1;
    if(severidade ==2):
        contadorSevero += 1;

porcentagemAssinto = ((contadorAssintomatico*100)/10);
porcentagemLeve = ((contadorLeve*100)/10);
porcentagemGrave = ((contadorSevero*100)/10);

print(f"Porcentagem de Assintomáticos = {porcentagemAssinto}");
print(f"Porcentagem de Sintomoas leves = {porcentagemLeve}");
print(f"Porcentagem de Sintomoas graves = {porcentagemGrave}");