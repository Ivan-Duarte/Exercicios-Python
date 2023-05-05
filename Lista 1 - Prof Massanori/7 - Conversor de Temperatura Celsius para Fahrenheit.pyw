#Converta uma temperatura digitada em Celsius para Fahrenheit.
#Formula F=9*C/5+32


#Exemplo Input Usuario

tempcelsius = float(input("Insira a Temperatura em Celsius: "))
conversaof = (9*tempcelsius)/5 + 32
print (f"O valor convertido é de:{conversaof:.2f} Graus Fahrenheit")


