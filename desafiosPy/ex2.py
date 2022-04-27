agenda = {'wilson':"92319125", 'cleber':" 92654781", 'wamudo':"91365478", 'sthe': "45897623", 'vitinho': "78962135", 'bia': "895314258", 'leo':"636251056",'doná':"77777777",'tify': "12335564", 'jaqcin': "566582482455"}
while True:
    letra = str(input("Digite uma letra: ")).lower()
    for nome in agenda.keys():
        if nome[0] == letra:
            print(nome)
    print("Não existe/exitem mais nomes")
    num = str(input("Digite 2 números: "))
    while True:
        if len(num) == 2:
            break
        else:
            print("Valor inválido")
            num = str(input("Digite 2 números: "))
            continue
    for numero in agenda.values():
        if numero[0] == num[0] and numero[-1:] == num[1]:
            print(numero)
    print("Não existe/exitem mais numeros")

    op = int(input("Continuar? 1-S/2-N: "))
    if op == 1:
        continue
    elif op == 2:
        break