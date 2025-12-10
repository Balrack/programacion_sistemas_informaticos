#Ejercicio61.py

#Me pida por consola un codigo, si el codigo es correcto es decir "==", me aparezca por pantalla
#el mensaje "Codigo correcto, puede pasar", si es incorrecto "Codigo erroneo, alerta!!!!"

codigo=int(input("Ingresa el codigo correcto: "))
codigoSecreto=0000
if codigo==codigoSecreto:
    print("Codigo correcto, pasa maquina")
else:
    print("NO PUEDES PASAR(con voz de Gandalf)")
