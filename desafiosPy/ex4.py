import time
lanches = {
    "lanche1": "x-salada sem salada",
    "lanche2": "x-egg sem ovo",
    "lanche3": "x-bacon sem bacon"
}
bebidas = {
    "Bebida1": "Whisky",
    "Bebida2": "Red Bull",
    "Bebida3": "Refrigerante"
}
sobremesas = {
    "Sobremesa 1": "Pão doce",
    "Sobremesa 2": "Coockies",
    "Sobremesa 3": "7 Belo"
}
pedido = []

def pedidoLanche():
    print(lanches)
    while True:
       lanche = int(input("Escolha seu lanche ou digite '4' para pular: "))
       time.sleep(1)
       if lanche == 1:
            pedido.append(lanches['lanche1'])
            break
       elif lanche == 2:
             pedido.append(lanches['lanche2'])
             break
       elif lanche == 3:
            pedido.append(lanches['lanche3'])
            break
       elif lanche == 4:
           break
       else:
            print("Digita o bang direito")
            continue
def pedidobebida():
    print(bebidas)
    while True:
        bebida = int(input("Escolha sua bebida ou digite '4' para pular: "))
        time.sleep(1)
        if bebida == 1:
            pedido.append(bebidas['Bebida1'])
            break
        elif bebida == 2:
            pedido.append(bebidas['Bebida2'])
            break
        elif bebida == 3:
            pedido.append(bebidas['Bebida3'])
            break
        elif bebida == 4:
            break
        else:
            print("Digita o bang direito")
            continue



def pedidosobremesa():
    print(sobremesas)
    while True:
        sobremesa = int(input("Escolha sua sobremesa ou digite '4' para pular: "))
        time.sleep(1)
        if sobremesa == 1:
            pedido.append(sobremesas['Sobremesa 1'])
            break
        elif sobremesa == 2:
            pedido.append(sobremesas['Sobremesa 2'])
            break
        elif sobremesa == 3:
            pedido.append(sobremesas['Sobremesa 3'])
            break
        elif sobremesa == 4:
            break
        else:
            print("Digita o bang direito")
            continue
def pedido3():
    pedidoLanche()
    pedidobebida()
    pedidosobremesa()
def finalizarpedido():
    while True:
        time.sleep(1)
        print(pedido)
        time.sleep(1)
        yon = str(input("O(s) pedido(s) está correto? S/N ")).upper()
        if yon == "S":
            break
        elif yon == "N":
            pedido.clear()
            pedido3()
            continue
    while True:
        time.sleep(1)
        print(pedido)
        time.sleep(1)
        yon2 = str(input("Deseja adicionar mais alguma coisa? S/N ")).upper()
        if yon2 == "S":
            pedido3()
            continue
        elif yon2 == "N":
            break

def inico():
    print("-"*50)
    print("Lanchonete do Wilsão  ( ͡° ͜ʖ ͡°)")
    time.sleep(1)
    print("Escolha seu pedido: ")
    time.sleep(1)

while True:
    pedido.clear()
    inico()
    pedido3()
    finalizarpedido()
    with open('comanda.txt', 'w') as arquivo:
        arquivo.write(str(pedido))
    time.sleep(1)
    print(pedido)
    time.sleep(1)
    yon2 = str(input("Deseja mais alguma coisa? S/N ")).upper()
    if yon2 == "S":
        continue

    elif yon2 == "N":
        break
print("Volte sempre ( ͡◉ ͜ʖ ͡◉)")