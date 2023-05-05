#Converta uma temperatura digitada em Fahreneit para Celsius.
#Formula : Celsius = Fahrenheit - 32 * 5/9

tempfahren = float(input("Insira a Temperatura em Fahrenheit: "))
tempconvertida = (tempfahren-32) * 5/9
print (f"A temperatura convertida é de:{tempconvertida:.2f} Graus Celsius")
