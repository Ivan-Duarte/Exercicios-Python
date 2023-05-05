#Solicite o preço de uma mercadoria e o percentual de desconto.
#Exiba o valor do desconto e o preço a pagar.

# Valor da Mercadoria
# Valor do Desconto
# Mercadoria com Desconto

mercadoria = float(input("Insira o Preço do Produto: "))
desconto = float(input("Insira o Valor de Desconto: "))
precodesconto = (mercadoria*desconto)/100
precofinal = (mercadoria - precodesconto)
print ("O valor do produto com desconto é de: ", precofinal," O valor do desconto é de: ", precofinal)

