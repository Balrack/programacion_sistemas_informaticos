#Ejercicio 3 Avanzado
#quiero esto usando input:
# importe: 100
#descuento 10%: 10
#total importe=100-10
# iva: 21 sobre el total importe
# total a pagar: total importe+iva

importe=int(input("Introduce el importe: "))
descuento=0.10

descApli=importe*descuento

descCal=importe-descApli
iva=0.21

ivaCal=descCal*iva


totalCal=ivaCal+descCal
print("El descuento aplicado es: ",descCal)
print("El iva aplicado es: ", ivaCal)
print("El total a pagar importe con descuento + iva ", totalCal)