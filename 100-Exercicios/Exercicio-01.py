def area(x,y):
    resultado = (x*y)
    return resultado

def perimetro(x,y):
    resultado = (x*2+y*2)
    return resultado

x = int(input("Insira a altura: "))
y = int(input("Insira a largura: "))

#resultArea = area(10, 5)
#resultPerimetro = perimetro(10, 5)
#print("Sua area é igual a: ",resultArea)
#print("Seu perimetro é igual a: ",resultPerimetro)

print("Sua area é igual a: ", area(x, y))
print("Seu perimetro é igual a: ", perimetro(x, y))
