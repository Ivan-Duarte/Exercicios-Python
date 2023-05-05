#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário
#Assim como a quantidade de dias pelos quais o carro foi alugado.
#Calcule o preço a pagar,sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.


#Kilometros Percorridos -> R$ 00,15 km rodado
#Quantidade de Dias     -> R$ 60,00 Dia

kmpercorrido = float(input("Insira quantos quilometros o carro percorreu: "))
diasalugado = float(input("Insira a quantidade de dias alugado: "))
totalpagar = (0.15*kmpercorrido) + (60.00*diasalugado)
print (f"Sua conta final é de: R${totalpagar:.2f}")
