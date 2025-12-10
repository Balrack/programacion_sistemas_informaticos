#1º Tiene que pedirme el importe y las unidades, usando el total resultante
#Si el total es menor de 100, 0% descuento
#			Entre 101 y 1000 5% descuento
#			Entre 1001 y 2000 10% descuento
#			>2000 20% descuento
#Ejemplo: 
#Importe: 1000
#Unidades: 1
#Total: 1000
#Descuento: 50
#total a pagar: 950

valorImp=int(input("Ingresa el importe "))
unidades=int(input("Introduce las unidades "))
descuento=0
imporTotal=valorImp*unidades

if imporTotal<=100:
    print(f"El total a pagar es {imporTotal}")
else:
    if imporTotal>101 and imporTotal<=1000:
        descuento=0.05
    if imporTotal>1001 and imporTotal<=2000:
        descuento=0.1
    if imporTotal>2000:
        descuento=0.2
        
print("El importe a pagar es " , imporTotal - (imporTotal*descuento))
