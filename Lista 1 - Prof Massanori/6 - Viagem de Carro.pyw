#Calcule o tempo de uma viagem de carro.
#Pergunta a distância a percorrer e a valocidade média esperada para a viagem.

#Distancia a percorrer
#Velocidade média
# 1 hora = 60 minutos

#Input Exemplo
#100 Km Distancia
#50 Kmh
#Resultado = 2h

distancia = float(input("Insira a Distancia: "))
velocidademedia = int(input("Insira a Velocidade Média: "))
tempoviagem = (distancia/velocidademedia)
print ("Sua viagem durará: ",tempoviagem," horas")




