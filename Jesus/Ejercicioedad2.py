#de 0 a 3 bebe
#3 a 10 niño
#10 a 13 preadolescente
#13 a 17 adolescente
#18 a 67 trabajador
#a partir de 67 Feliz Jubilado

#limite 120 años

edad=int(input("Pon tu edad: "))

if edad<0 or edad>=120:
    print("Incorrecto")
else: 
    if edad>=0 and edad <3:
        print("Hola bebe")
    if edad>=3 and edad <=10:
        print("niñ@")
    if edad>10 and edad <=13:
        print("Preadolescente")
    if edad>13 and edad <=17:
        print("Niñato")
    if edad>17 and edad<=67:
        print("Trabajador, o no ")
    if edad>67:
        print("Jubileta")
        