#Carga por consola del nombre edad y altura de dos personas y mostrar el nombre del mas alto
print("Datos de la primera persona")
nombre1=input("Ingrese nombre: ")
edad1=int(input("Ingrese edad: "))
altura1=float(input("Ingrese la altura: "))

print("Datos de la segunda persona")
nombre2=input("Ingrese nombre: ")
edad2=int(input("Ingrese edad: "))
altura2=float(input("Ingrese la altura: "))

print("La persona mas alta es: ")
if altura1>altura2:
    print(nombre1)
else:
    print(nombre2)
    