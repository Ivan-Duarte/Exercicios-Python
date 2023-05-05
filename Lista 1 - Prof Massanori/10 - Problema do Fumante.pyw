#Escreva um programa para calcular a redução do tempo de vida de um fumante.
#Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
#Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá.
#Exiba o total de dias.

#Cigarros Por Dia
#Anos Fumando

# 1      Cigarro  = - 10 Minutos
# 6      Cigarros = -  1 Hora
# 144    Cigarros = -  1 Dia
# 52.560 Cigarros = -  1 Ano

#Input Usuario
#1 Cigarros, 1 Ano = 
#converte para minuto, divide pelo dias
#--------------------------------------------------

cigarrodia = int(input("Insira quantos cigarros fuma por dia: "))
anosfumando = int(input("Insira quantos anos já é fumante: "))
anoperdido = anosfumando*365
minutoperdido = (cigarrodia*10)*anoperdido
horaperdida = minutoperdido/60
diaperdido = horaperdida/24
print (f"Você Perdeu: {diaperdido:.1f} dias de vida seu OTÁRIO!!!")
print ("Larga essa Poha desse cigarro")

#--------------------------------------------------

#Codigo Prof. Massanori

#q_cig = int(input('Por favor, insira a quantidade de cigarros fumados por dia: '))
#q_ano = int(input('Agora insira a quantidade em anos que vocÃª Ã© fumante: '))
#t_dias = q_ano * 365
#t_cig = q_cig * t_dias
#perda_vida = t_cig / 144
#print(f'VocÃª perdeu {perda_vida:.1f} dia/s da sua vida. ')


