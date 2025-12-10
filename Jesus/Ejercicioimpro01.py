#Ejercicio 1
# quiero que me pida con un input un importe, 
# me calcule el iva y me de el total(importe+iva)

importe=float(input("Introduce el importe: "))
iva=0.21
ivaCal=importe*iva
totalIva=importe+ivaCal

print("El iva calculado es: ", ivaCal)
print("El importe total + iva es: ",totalIva)

