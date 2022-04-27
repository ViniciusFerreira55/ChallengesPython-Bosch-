dia_inicio_ferias = 17
dia_final_ferias = 31
mes = "Dezembro"
ano = 2021
print("As férias serão retiradas entre o dia", dia_inicio_ferias, " e o dia ", dia_final_ferias, " do mês de ", mes, "do ano de", ano)
print("As férias serão retiradas entre o dia {}  e o dia  {} do mês de {} do ano de {}".format(dia_inicio_ferias,dia_final_ferias,mes,ano))

print("R$ {:10.1f}".format(10000.00))
print("R$ {:010.2f}".format(1.11))

num1 = 9
num2 = "11"
produto = num1 * num2
print(produto)


for i in range(1,8):
    if(i == 5):
        continue
    print(i)
