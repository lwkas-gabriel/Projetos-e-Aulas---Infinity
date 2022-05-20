dia = int(input("Inserir dia do mês: ")) #entradas válidas = 1 - 31#
mes = int(input("Inserir mês: ")) #entradas válidas = 1 - 31#

if(dia <= 0 or mes <=0 or dia >=32 or mes >=13):
    print("entradas inválidas"); #tratando valores que não me interessam#
else:
    if(dia >= 21 and mes==3) or (dia <= 20 and mes==4): print("Seu signo é Áries");
    elif(dia >= 21 and mes==4) or (dia <= 20 and mes==5): print("Seu signo é Touro");
    elif(dia >= 21 and mes==5) or (dia <= 20 and mes==6): print("Seu signo é Gêmeos");
    elif(dia >= 21 and mes==6) or (dia <= 22 and mes==7): print("Seu signo é Câncer");
    elif(dia >= 23 and mes==7) or (dia <= 22 and mes==8): print("Seu signo é Leão");
    elif(dia >= 23 and mes==8) or (dia <= 22 and mes==9): print("Seu signo é Virgem");
    elif(dia >= 23 and mes==9) or (dia <= 22 and mes==10): print("Seu signo é Libra");
    elif(dia >= 23 and mes==10) or (dia <= 21 and mes==11): print("Seu signo é Escorpião");
    elif(dia >= 22 and mes==11) or (dia <= 21 and mes==12): print("Seu signo é Sagitário");
    elif(dia >= 22 and mes==12) or (dia <= 20 and mes==1): print("Seu signo é Capricórnio");
    elif(dia >= 21 and mes==1) or (dia <= 18 and mes==2): print("Seu signo é Aquário");
    else: print("Peixes");