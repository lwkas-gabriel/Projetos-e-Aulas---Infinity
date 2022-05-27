numeroSecreto = 255;

guess = 0;

while numeroSecreto != guess:
    guess = int(input("inserir numero: "));
    if numeroSecreto != guess:
        print("erro! numero inválido");
    else:
        print("parabéns, você acertou! O numero secreto era ", numeroSecreto);