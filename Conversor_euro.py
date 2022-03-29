menu = """
Bienvenido al Conversor de Monedas

1 - Pesos Colombianos
2 - Pesos Argentino
3 - pesos Mexicano

Elige una Opcion: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("Cuantos pesos Colombianos tienes ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares= str(dolares)
    print("Tienes $ "+ dolares + "dolares")
elif opcion == 2:
    pesos = input("Cuantos pesos Argentinos tienes ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares= str(dolares)
    print("Tienes $ "+ dolares + "dolares") 
elif opcion == 3:  
    pesos = input("Cuantos pesos Mexicanos tienes ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares= str(dolares)
    print("Tienes $ "+ dolares + "dolare")     
else: 
    print("Ingrese una opcion correcta por favor ")
    