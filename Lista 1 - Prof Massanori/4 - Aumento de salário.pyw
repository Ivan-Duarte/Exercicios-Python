#Faça um programa que calcule o aumento de um salário.
#Ele deve solicitar o valor do salário e a porcentagem do aumento.
#Exiba o valor do aumento e do novo salário.

#Valor do salario
#Valor do Aumento
#Valor do salario + aumento

salarioatual = float(input("Insira o valor do salário: "))
aumento = float(input("Insira o valor do aumento em %: "))
#Para calcular a porcentagem, deve primeiro multiplicar a porcentagem pelo valor e depois dividir por 100.
reajuste = (salarioatual*aumento)/100
#Para ter o valor total do salário, deve somar o valor do reajuste com o salario atual.
salariocorrigido = (reajuste + salarioatual)
print ("O salario com aumento é de: ",salariocorrigido," O valor do aumento é de: ",reajuste)
