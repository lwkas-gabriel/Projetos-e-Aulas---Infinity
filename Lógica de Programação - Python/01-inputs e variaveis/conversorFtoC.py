#conversor de fahrenheit para celsius

tempFahr = float(input("Inserir temperatura Fahrenheit: "));

primeiroCalculo = 5*(tempFahr-32);
segundoCalculo = primeiroCalculo/9;

print("A temperatura celsius correspondente é: ",segundoCalculo);