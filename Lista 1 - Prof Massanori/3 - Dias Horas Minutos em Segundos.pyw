#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

# Dia    = 24 horas
# Hora   = 60 Minutos
# Minuto = 60 Segundos

# 1 Dia    = 86.400 segundos
# 1 Hora   = 3.600 segundos
# 1 Minuto = 60 segundos

dia = int(input("Insira a Quantidade de Dias: "))
hora = int(input("Insira a Quantidade de Horas: "))
minuto = int(input("Insira a Quantidade de Minutos: "))
segundo = int(input("Insira a Quantidade de Segundos: "))
diasegundo = (((dia*24)*60)*60)
horasegundo = ((hora*60)*60)
minutosegundo = (minuto*60)
total = (diasegundo + horasegundo + minutosegundo + segundo)
print ("A conversão dos valores para segundo é de: ",total,"segundos")
