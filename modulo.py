
print("Bienvenido a ... ")
print("""
|/////////////// |   |   //////////////
|                |   |          |         | |
|                |   |          |        |   |
|/////////       |   |          |       | ///  |
|                |   |          |      |        |
|                |   |          |     |          |
|

""")

# Solicitud de nombre
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()

# CÃ¡lculo de edad
año = int(input("Para preparar tu perfil, dime en que año naciste. "))
edad = 2021-año
print()

# CÃ¡lculo de estatura
estatura = float(input("Cuentame mas de ti, para agregarlo a tu perfil. ¿Cuanto mides? Da­melo en metros,por ej:1,53mtrs. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

# Cantidad de amigos
num_amigos = int(input("Muy bien. Finalmente, Cuentame cuantos amigos tienes. "))
# genero =str(input("dinos tu genero"))
# if genero == "F" or genero == "f" or genero == "":
#     mensaje = input("femenino bien ")
# elif Mensaje =="H" or escribir=="h":
    
#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centi­metros")
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la informacionn. Esperamos que disfrutes con Mi Red")
print()

#Usaremos una variable bool para indicar si el usuario desea continuar
#utilizando el programa o no
continuar = True

#Este ciclo se mantiene en ejecuciÃ³n hasta que el usuario desee salir
while continuar:

    #Solicitamos opciÃ³n al usuario
    escribir_mensaje = str(input("Â¿Deseas escribir un mensaje? (S/N) "))
    #Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
    if escribir_mensaje == "S" or escribir_mensaje == "s" or escribir_mensaje == "":
        mensaje = input("Vamos a publicar un mensaje. Â¿Que piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")
    #En caso que sea otra respuesta, vamos a decidir salir.
    #AsÃ­, en la siguiente iteraciÃ³n el ciclo terminarÃ¡
    elif escribir=="N" or escribir=="n":
      continuar = False
#Mensaje de salida, una vez que el ciclo ha terminado.
print("Gracias por usar Mi Red. ¡Hasta pronto!")
#   Por ejemplo, puedes agregar una acciÃ³n que permita al usuario modificar su nombre.
