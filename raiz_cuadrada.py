print("")
print("Raiz Cuadrada de un Numero")
print()
respuesta = False
while respuesta == False:
    b = float(input("Raiz cuadrada de No. "))
    a = float(b ** (1/2))
    print()
    print(" Resusltado de la raiz de" ,b, " = " , round(a , 2))
    pregunta = input(" Desea sacar la  raiz a otro numero, S o N ")
    if pregunta == "N":
        respuesta = True
        print()
        print("FIN")
