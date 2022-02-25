#aca el + sirve para unir las palabras sin string con su espacio correspondiente (concatenacion)
print ("hola" + " sofia")
#ACLARACION EL + ES PARA UNIR COSAS IGUALES Y LA , ES PARA UNIR !=
#las listas pueden tener distintos elementos dentro o todos iguales(listas) y se usa []
#(tuplas) se escriben con {} y los datos no se pueden cambiar
mis_datos:{
"nombre":"sofia",
"apellido":"blet",
"edad":"20" #sin coma el ultimo
}
print(type({"nombre"}))#ahi veo el tipo q es lo q pongo( si o si igual copiado)
#variables para ahorrar espacio
#VARIABLES SIMEPRE CON EL =
x =100
book ="el libro de la selva"
#mas facil en una sola linea como el de abajo
x,book = 100,"el libro de la selva"
#ejemplo
nombre,apellido,edad= "sofia","blet","20" #ej de mis_datos en forma de variables
#ambas formas se pueden hacer y da igual
print(type({x,book}))
print(x)
print(book)
#poner en mayusculas una variable hace q sea constante y nunca puede cambiar
PI: 3.14
#str
frase ="hola fiita xd"
print(frase.upper())#veo todo en mayusculas
print(frase.lower())#minuscula
print(frase.swapcase())#pasa de mayusculas a minuscula o al revez
print(frase.capitalize())#1er letra
print(frase.replace("hola","hello"))#remplazo por otra
#ej
#print(frase.add("agrego esto"))
print(frase.replace("a","o"))#solo esa me reemplaza
print(frase[0])#me devuelve el valor en esa posicion
print(frase.count("a"))# veo la cantidad q hay del valor a,ojo con las MAYUSCULAS,valen otro
print(frase.count(" "))#sin nada veo cuantos espacios totales hay incluido el(vacio)
print(frase.strip())#saca espacios al pedo
# veo lo que hay en su posicion => print(amor[3])
#print(amor.strip())#ahora saca los espacios pero si no lo pongo en la pantalla veo vacio pq eso habria en la posicion 3

print(frase.startswith("hola"))#veo true o false si empieza con hola
print(frase.endswith("xd"))#veo si termina con eso o no
print(len(frase))#total de caracteres con el vacio incluido
print(len("cuantos caracteres tiene eso aca"))#veo de esa frase
#ejemplo
frase_ej = "chori"
print("mi nombre es sofia pero me dicen " + frase_ej.upper())
#otro ej pero sin usar +(es lo mismo igual)
x,y= "hola","fiita"
print(x,"gracias por estar aqui ",y )#los valores q quiero ver no pongo ""
#EXTRA
rica="Vas a ser rica "
print(rica*6)
#otro ej
print(" AMATE " * 4)
#pido datos al usuario con input y fijarse el espacio
print("ponga cuantos ex tiene")
EX = input("")#eso nos dice
cantidad_ex = int(EX) +1
print("usted tuvo en total de exs ")
print(cantidad_ex)
#cuentas
x,y=2,2
rta=x+y
print(rta)#sin"" pq no es str y ademas estamos con var
#ej en la misma operacion
x=1#aca la x cambia de valor por eso la operacion da distinto
rta=x+y
print(rta)
x,y= 4,2
rta=x*y #multiplicacion simple
print(rta)
x,y= 4,2
rta=x/y# DA DECIMAL el resto de la 1era y 2da division(toda la cuenta hasta con decimales)
print(rta)
x,y= 4,2
rta=x**y #exponete
print(rta)
x,y= 4,2
rta=x//y #division simple
print(rta)
x,y= 4,2
rta=x%y #da 0???
print(rta)
#ACLARACION LAS CUENTAS DEBEN CUMPLIR EL ORDEN (PROPIEDADES)
# != distinto
# == igual
# and y
#or o
#not no
#defino que es el valor sin serlo
str(15)#ya digo q es str sin ""
int(2.6)#ya digo q es entero aunque sea con coma
#ej
OK=int(4.3)+float("3")
print(OK)#Aca sumamos entero con decimal por eso con coma
#int con int
hola=int("2")+15#es un int NO STR pq lo aclaro
print(hola)
#str con str da TODO junto
caca=str(2)+str(15)#da 215
print(caca)
#float con float
lol=float(1)+10.2
print(lol)
# F
bool(0)
bool("")
#veo varios print uno abajo de otro
nombre,edad="fiita",20
print("soy", nombre,end=" blet")#con el end agrego es normal y con el SEP si veo en != lineas
print("y tengo",edad,"años")
print("recien cumplidos")
#otro ej
nombre,año="fiita","20"
print("hola soy " + nombre , end=" blet"  + " y tengo " + año + " años.")
pais,estado="argentina","soltera"
print(" Soy de " + pais + " y estoy " + estado)
#ej de mi edad CORRECTO
ahora = int(input(" dime tu año de nacimiento?: "))#ponemos el int para q sea si o si entero lo q usemos
total=2020#año de ahora
edad= total-ahora
print(" tenes ", edad," años")
#practica
mi_moneda=float(input("hola!Dinos cuanto dinero tienes :"))
valor_dolar=173
mivalor=mi_moneda/valor_dolar
mivalor=round(mivalor, 3)#los decimales son 3
print("tu posees en dolares : ", mivalor)
#uso de funciomes
menu = """
bienvenido eliga su moneda a pasar a dolares:
1-argentina
2-colombia
3-mexico
elige el que quieras"""
opcion = int(input(menu))
if  opcion == 1:#siempre "" salvo q aclare q usa int
     peso = input("dime tu dinero " )
     peso = float(peso)
     dolar_arg = 195
     dolar = peso / dolar_arg
     dolar = round( dolar , 2)#con 2 decimales
     dolar = str(dolar)
     print("tienes en total $ "+ dolar + " dolares" )
elif opcion == 2:
    peso = input("dime tu dinero colombiano " )
    peso = float(peso)
    dolar_col = 3785
    dolar = peso / dolar_col
    dolar = round( dolar , 2)#con 2 decimales
    dolar = str(dolar)
    print("tienes en total $ "+ dolar + " dolares" )
elif opcion == 3:
    peso = input("dime tu dinero mexicano " )
    peso = float(peso)
    dolar_mex = 24
    dolar = peso / dolar_mex
    dolar = round( dolar , 2)#con 2 decimales
    dolar = str(dolar)
    print("tienes en total $ "+ dolar + " dolares" )
else:
    print("pon algo valido eh")
#otro ej
def suma(a, b):
    print("se suman 2 numeros")
    rta = a + b
    return rta #regresa el valor de la funcion
total = suma(1, 4)
print(total)
#ej reducido de la moneda
def convertor(tipo_pesos, valor_dolar):
     #conviene crear las funciones arriba de TODO mi codigo(LAS DEFINO Y LUEGO LAS INVOCO)
    peso = input("dime tu dinero " + tipo_pesos + " tienes " )
    peso = float(peso)
    dolar = peso / valor_dolar
    dolar = round( dolar , 2)#con 2 decimales
    dolar = str(dolar)
    print("tienes en total $ "+ dolar + " dolares" )

menu = """
bienvenido eliga su moneda a pasar a dolares:
1- argentina
2- colombia
3- mexico
elige el que quieras  """
opcion = int(input(menu))
if  opcion == 1:#siempre "" salvo q aclare q usa int
     convertor("argentinos",195)
elif opcion == 2:
    convertor("colombianos",3785)
elif opcion == 3:
    convertor("mexicanos",25)
else:
    print("pon algo valido eh")
#palabras iguales al revez
#palindromo= se lee igual de atras a adelante
def palindromo(dato):
    dato = dato.replace(" "," ")#elimina espacios
    dato = dato.lower()#pq es !0 con mayusculas
    dato_invertido = dato[::-1]
    if dato == dato_invertido:
        return True
    else:
        return False

def run():
    dato = input("pon una frase y te digo si es palindromo: ")
    es_palindromo = palindromo(dato)
    if es_palindromo == True:
        print("si que lo es eh")
    else:
        print("no lo es ok")


if __name__ == "__main__ ":
    run()
#mejor asi
def run():
    palabra = str(input("Escribe un palabra: ")).lower().replace(' ', '')#pido dato,lo paso a minusculas y saco es espacio
    if palabra[::] == palabra[::-1]:
        print('Es palíndromo')
    else:
        print('No es palíndromo')


if __name__ == '__main__':
    run()
#ciclo while
def run():
    LIMITE = 1000#PQ ES CTE
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:#menor
        print("2 elevado a " + str(contador) +  " es igual a: " + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador

if __name__ == '__main__':
    run()
#for y while
contador = 1
print(contador)
while contador < 3:
    contador = contador + 1
    #es lo mismo que: contador += 1
    print(contador)
#con el ciclo for lo hago en 2 lineas
for contador in range(10):#un rango de 10 numero empezando del 0 son ya 10 por eso hasta el 9
    print(contador)
# ej de tabla del 11
for i in range(10):
    print(11*i)
#mi nombre largo abajo de cada letra
def run():#veo mi nombre separando las cadenas una abajo de otra
    nombre = input("tu nombre es? :")
    for letra in nombre :
        print(letra)#puedo poner en mayusculas y todo eso tambien
if __name__ == '__main__':
    run()
#para las buenas practicas
#def run():
    #pass
#if __name__ == '__main__':
    #run()
#veo los numeros pares del ciclo
def run():
    for contador in range (10):
        if contador %2 != 0:#veo los pares
            continue#lo q siga despues no lo lee y sigue con el ciclo nomal
        print(contador)

if __name__ == '__main__':
    run()
#adivinar en numeros
import random #sirve para aleotorio
def run():
    num_misterioso = random.randint(1, 10)
    numero = int(input("elige un numero del 1 al 100 "))
    while numero != num_misterioso:
        if numero < num_misterioso:
            print("es menor subele mas")
        else:
            print("pon uno mas mini")
        numero = int(input("elige otro :"))
    print("GANASTE FIITA")

if __name__ == '__main__':
    run()
#ej
def run():
    diccionario = {
    "llave1" : 1,
    "llave2" : 2,
    "llave3" : 3,
    }
    #print(diccionario["llave1"])
    población_paises = {
	'Argentina': 44_938_712,
	'Brasil': 210_147_125,
	'Colombia': 50_372_424
}
# print(población_paises["argentina"])
    for pais in población_paises.keys():#veo los población_paises y con values veo lo q valen
        print(pais)
if __name__ == '__main__':
    run()
#contraseña
# import random
# def generar():
#     mayusculas = [ "A","B","C","D","G"]
#     minuscula = ["a","b","c","d","e"]
#     simbolos = ["#","#2","$","%","/"]
#     numeros = ["1","6","9","88","56","8"]
#     caracteres = mayusculas + minuscula + simbolos + numeros
#     password = []
#     for i in range(5):
#         caracteres_r = random.choice(caracteres_r) #al hazar
#         password.append(caracteres_r)
#     password = "".join(password)#un str de mi lista final
#     return password
# def run():
#     password = generar()
#     print("la nueva contra es: " + password )
# if __name__ == '__main__':
#     run()


import random
import string

def generar_contrasena():
    caracter = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase

    contrasena = []

    while (len(contrasena) < 16):
        caracteres=random.choice(caracter)
        contrasena.append(caracteres)

    contrasena = "".join(contrasena)
    return contrasena

def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: '+ contrasena)

if __name__ == "__main__":
    run()

#funcion de suma invocada
suma= lambda numeroa,numerob:numeroa + numerob
print(suma(10,30))
#usos del while para un bucle
count=4
while count <=10:
    print(count)
    count=count+1
#diccionario con  datos adentro
bombones={
"cantidad":1,
"precio":470,
"envio":330,
"marca":"felt-fort"
}
print(type(bombones))
#una lista que agrego un color en la posicion
lista_numerica = list((1,2,3,4))
color = ["red","blue"]
color[1]="violet"
print(color)
#condicionales con or not y and
x=25
y=20
if x>20 and x>=10:
    print("estas en el medio")
    if x>20 or x>20:
        print("eres mayor q 2 pero menor o igual a 20")
        if (not(x==y)):
            print("no eres igual a y")
