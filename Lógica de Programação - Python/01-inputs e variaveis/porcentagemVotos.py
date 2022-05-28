votosBrancos = int(input("Votos em Branco: "));
votosNulos = int(input("Votaram Nulo: "));
votosValidos = int(input("Votaram em algum candidato: "));

totalVotantes = votosBrancos + votosNulos + votosValidos;

porcentagemVotosBrancos = (votosBrancos*100)/totalVotantes;
porcentagemVotosNulos = ((votosNulos*100)/totalVotantes);
porcentagemVotosValidos = ((votosValidos*100)/totalVotantes);

print("Votos em branco: ",porcentagemVotosBrancos, "%");
print("Votos nulos: ", porcentagemVotosNulos, "%");
print("Votos Válidos: ", porcentagemVotosValidos, "%");
print("Total de votos", totalVotantes);