#pedir nota por consola y que indique si es aprobado o suspenso
nota=int(input("Ingresa tu nota: "))
if nota<0 or nota>10:
     print("Nota no valida")
else:
     
     if nota>0 and nota<5:
          print("Suspenso")
     if nota==5:
          print("Aprobado raspado")
     if nota==6:
          print("Bien")
     if nota==7 or nota==8:
          print("Notable")
     if nota==9 or nota==10:
          print("Sobresaliente")
          

    