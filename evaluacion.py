nombre=input("Hola usuario dime tu nombre por favor: ")
juego=input("Ahora "+ nombre+" dime tu juego favorito por favor: ")
datos=nombre + juego
print("usted es : "+ nombre+" y su juego favorito es " + juego)
print("A continuacion adivinare su edad OH YEAH PAPU")
nacimiento=int(input("Pon el año en el que naciste "))
ahora=2021
edad=ahora-nacimiento
print(" ADA CADABRA PATA DE CABRA,USTED TIENE " , edad , "AÑOS DE EDAD")
print("ahora te dire cuanto equivale tu moneda en pesos a dolares")
moneda_local=float(input("pon el dinero que posees en pesos argentinos "))
valor_dolar=159.02
equivalente=moneda_local/valor_dolar
equivalente=round(equivalente,3)
print("tu valor de los pesos a dolar es de " ,equivalente ," dolares totales")

menu=             """
ahora podra elegir
la moneda del
pais que usted desea
1-ARGENTINA
2-COLOMBIA
3-VENEZUELA
4-MEXICO           """

opcion=int(input(menu))
def convertor(tipo_pesos, valor_dolar):
    peso = input("dime tu dinero " + tipo_pesos + " que tienes " )
    peso = float(peso)
    dolar = peso / valor_dolar
    dolar = round( dolar , 3)
    dolar = str(dolar)
    print("tienes en total $ "+ dolar + " dolares" )
if opcion == 1:
    convertor("argentino",159.02)
elif opcion == 2:
    convertor("colombiano",3785)
elif opcion == 3:
        convertor("venezolano",200)
elif opcion == 4:
        convertor("mexicano",25)
else :
    print("PON ALGO REAL MANCO")
