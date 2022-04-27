pontos = []
times = []
cod = 0
while True:
    nome = str(input("Digite o nome do jogador: "))
    part = str(input("O jogador "+nome+" Jogou alguma partida: S/N")).upper()
    if part == 'S':
        qtnd = int(input("Quantas patidas esse jogador jogou? "))
        for i in range(1,qtnd+1):
            points = int(input(f"Quantos pontos o jogador {nome} fez na partida {i}: "))
            pontos.append(points)
    else:
        print('O jogador não jogou')
    times.append({"Cod": cod,"Jogador" : nome, "Pontos" : pontos[:]})
    pontos.clear()
    op = str(input("Continuar? S/N: ")).upper()
    if op == 'S':
        cod += 1
        continue
    else:
        break
print("Cod   Nome    Total     Pontos")
for i in times:
    print("{} {} {} {}".format(i['Cod'],i['Jogador'],sum(i['Pontos']),i['Pontos']))
indice = int(input("Digite o Cod do jogador: "))
for i,v in enumerate(times[indice]['Pontos']):
    print(f"No {i+1} set fez {v} pontos")