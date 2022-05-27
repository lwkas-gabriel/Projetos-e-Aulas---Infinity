media = 0;
totalNotas = int(input("inserir total de notas: "));

for num in range(1,totalNotas+1):
    media += int(input((f"inserir {num}ª nota: ")));
    if num == totalNotas:
        print(f"sua média é {media/num}");