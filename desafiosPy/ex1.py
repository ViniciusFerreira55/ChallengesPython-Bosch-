anos = {}
i = 0
anosel = 0
while True:
    chaves = str(input("Digite a chave: "))
    ano = int(input("Digite o ano: "))
    anos[chaves] = ano
    op = int(input("Continuar? 1-S/2-N: "))
    if op == 1:
        continue
    elif op == 2:
        break
print(anos)
indice = str(input("Digite o indice para ser verificado: "))
for i in anos.keys():
    if indice == i:
        anosel = anos[indice]
    if anosel%4 == 0 and anosel%100 != 0 or anosel % 400 == 0:
        print("O ano é bissexto")

    else:
        print("O ano não é bissexto")

    break

