c1 = (float(input("insira o primeiro numero ")))
tipo = (int(input("insira o sinal, 1 = Subtração, 2 = Soma, 3 = Multiplicação, 4 = Divisão ")))
c2 = (float(input("insira o segundo numero ")))
if(tipo == 1):
    res = (c1-c2)
elif(tipo == 2):
    res = (c1+c2)
elif(tipo == 3):
    res = (c1*c2)
elif(tipo ==  4):
    res = (c1/c2)
print(res)
