numeroSecreto = 5;

guess = -1;

while numeroSecreto != guess:
    guess = int(input("inserir numero: "));
    if numeroSecreto > guess:
        print("numero secreto é maior que o seu palpite");
    elif numeroSecreto < guess:
        print("numero secreto é menor que o palpite");
    else:
        print("parabéns, você acertou! O numero secreto era ", numeroSecreto);