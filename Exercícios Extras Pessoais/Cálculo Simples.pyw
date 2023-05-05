idpc1 = (str(input("Insira o Id da Peça 1: ")));
numpc1 = (int(input("Insira a Quantidade de Peças 1: ")));
valorpc1 = (float(input("Insira o Valor da Peça 1: ")));

idpc2 = (str(input("Insira o Id da Peça 2: ")));
numpc2 = (int(input("Insira o Quantidade de Peças 2: ")));
valorpc2 = (float(input("Insira o Valor da Peça 2: ")));

total = ((valorpc1*numpc1)+(valorpc2*numpc2));
print("VALOR A PAGAR: R$ {:.2f}".format(total));
