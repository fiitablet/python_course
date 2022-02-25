def imc(masa, estatura):
  # desde aquí hacia abajo debes modificar el programa
  # modifica la variable imc
  # recuerda que los datos están en las variables masa y estatura

 return masa / (estatura ** 2)
masa= float(input("escriba su masa en (kg) por favor: "))
estatura= float(input("escriba su estatura en (m) por favor: "))

indice = imc (masa, estatura )

print("su imc es :{}" .format(indice))

def velocidad(distancia, tiempo):
  return  (distancia / tiempo)
distancia= float(input("escriba su distancia en (km) por favor: "))
tiempo= float(input("escriba su tiempo en (h) por favor: "))

resultado=velocidad(distancia,tiempo)
print("su velocidad es :{}" .format(resultado))

meses = int(input("Ingresa nº de meses "))
if meses <= 12:
  print("No te daré miel")
else:
  print("Toma esta cucharada de miel")
x = 1
i = 0
while i < 4:
    x = x * 2
    i += 1 # es lo mismo que i = i + 1
print(x)

x = 48
y = 8
n = 0
while x > 0:
    x = x - y
    n = n + 1
print(n,"")
a = 5
b = 8
r = 0
while a > 0:
    r = r + b
    a = a - 1
print(r)
a = 4
b = 3
r = b
while a > 1:
    a = a - 1
    b2 = b
    r2 = 0
    while b2 > 0:
        r2 = r2 + r
        b2 = b2 - 1
    r = r2
print(r)
a = 3
for i in range(2, 3):
    a = a * i
print(a,"")
a = 2
for i in range (1,4):
    a = i ** a
# print(a)
for i in range(10):
    print('hola mundo')
a = 0
for i in range(3):
    a = a + i
# print(a)
numero = 1
while numero <= 5:
  print(numero, numero**2)
for i in range(1,101):
 for j in range(1,101):
    print(i,j)

def es_primo(numero):
  primo = True
  # aquí debes implementar tu código
  # modificando la variable primo
  # (no modifiques nada de las lineas anteriores)
primo = int(input("Ingresa un numero del a al 10 y te digo si es primo o no "))
if primo == 2  and 3 and 5 and 7 and 11:
      print("  no sos primo")
else:
    print("si sos primo")


continuar = True
opcion = -1
while opcion != 0:
    opcion=int(input("Elija opcion 1, 2 o 0 (salir):"))
    if opcion == 1:
        print("Ejecutamos la opcion 1")
    elif opcion == 2:
        print("Ejecutamos la opcion 2")
    elif opcion == 0:
        print("Has decidido salir.")

continuar = True

while continuar:
  #Solicitamos opción al usuario
  escribir = str(input("¿Deseas escribir un mensaje? (S/N) "))
  if escribir=="S" or escribir=="s" or escribir=="":
    mensaje = input("¿Qué piensas hoy? ")
    print(nombre, "dice:", mensaje)
  elif escribir=="N" or escribir=="n":# O IF Y LO MISMO
    continuar = False

    continuar = False
negocios
Ejecutivo: 90

Jefe: 100

Externo: 50



def imc(masa, estatura):
 return masa / (estatura ** 2)
masa= float(input("escriba su masa en (kg) por favor: "))
estatura= float(input("escriba su estatura en (m) por favor: "))
indice = imc (masa, estatura )

print("su imc es :{}" .format(indice))

def sueldo(cargo):
  cargo = 100
  # aquí debes implementar tu código
  # modificando la variable dinero
  # (no modifiques nada de las lineas anteriores)
  Ejecutivo = True
  cargo = str(input(" escriba su cargo : "))
if Ejecutivo== True :
    print("su suldo es de 90")
elif  jefe == True:
        print("su cargo es de jefe y de 100")
else:
        print("su cargo es de externo y de 50")
            #return cargo
def funcion_misteriosa(x):
  for i in range(2,x):
    if x%i==0:
      return False
  return True
def funcion_misteriosa(x):
  c=0
  while x!=0:
    c+=1
    x = x//10
  return c
def suma(N):
    s=int(input("pon algo"))
s=1
for i in range(N):
    s+=i
return s
def sumador(n, sumando):
  sumando += 1
  n += sumando
  return n
b = 9
s = "Acaso hubo buhos aca"
t = s[2:9]+s[0:1]
print(t)

def mcd( x, y):
    mcd = 1

    if x % y == 0:
        return y

    for k in range(int(y/2),0, -1 ):
        if x % k == 0  and y  % k == 0:
            mcd = k
            break
        return mcd
print(mcd(10,15))
def imc(masa, estatura):
    return masa / estatura ** 2
masa= float(input("escriba su masa en (kg) por favor: "))
estatura= float(input("escriba su estatura en (m) por favor: "))
indice = imc (masa, estatura )

print("su imc es :{}" .format(indice))

def velocidad(distancia, tiempo):
 #resultado = ""
 return distancia/tiempo

tiempo=1 #segundo
distancia=0.01 # kilometro
velocidadMS=(velocidad(distancia,tiempo)*1000)
velocidadKH=(((velocidadMS)*3600/1000)*1)
resultado=("La Velocidad es de " + str(velocidadKH) + " km/h o " + str(velocidadMS) + " m/s")
print(resultado)

def sueldo(cargo):
    if cargo== "Externo":
        print("dinero= 50")
if cargo== "Ejecutivo":
 print("dinero= 90")
if cargo== "Jefe":
  print("dinero= 100")
  return sueldo
a = open("mooc.txt", "w")
a.write("1 2 3 4")
a.write("5 6 7 8")
a.close()


def es_primo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def app():
    num = int(input('escribe un numero: '))
    result = es_primo(num)

    if result is True:
        print('es primoo!!')
    else:
        print('no es primo!!')





def intercalar(string_a, string_b):
    i = 0
    cadena = ""
    while(i < len(string_a)):
        cadena += string_a[i] + string_b
        i = i + 1
    return cadena

print(intercalar("string_a", "string_b"))

def remover_enesimo(s, n):
   return s[:n]+s[(n+1):]

frase = int(raw_input("Escribe tu frase o palabra: "))
indice = int(raw_input("Escribe el índice: "))
print (remover_enesimos(frase, indice))


unidades = [40, 32, 49, 2, 20, 8, 55, 300, 10]
muestra = unidades[2]+unidades[3:7:3]+unidades[7]
print (muestra)
votos =resultados = [ ["Alfredo",20], ["Marcela",40], ["Ignacio",30], ["Loreto",10] ]
mayoria = ganador(resultados)
def ganador(votos):
  mayor = votos[len(votos)-1]
  for cand in votos:
    if cand[1] >= mayor[1]:
      mayor = cand
  return mayor


nuevo = input("Indica el nombre de tu nuevo amigo o amiga: ")
agregar_amigo(lista_amigos, nuevo)
def agregar_amigo(lista_amigos, nuevo_amigo):
  lista_amigos = lista_amigos + nuevo_amigo
  print("agregar_amigo")
  return lista_amigos
def mostrar_estados_amigos(lista_amigos):
  for amigo in lista_amigos:
    archivo = open(amigo+".user", "r")
    for i in range(7):
      linea = archivo.readline().rstrip()
      print(amigo+":", linea)
    archivo.close()
def es_primo(numero):
    es_primo = True
    for i in range(2,numero):
        if numero//i == 0:
            es_primo = False
    return es_primo
print(es_primo(1))
print("dime tu num")
numero= int(input("¿Qué número quieres saber si es primo? "))
valor= range(2,numero)
contador = 0
for n in valor:
  if numero % n == 0:
    contador +=1
    print("divisor:", n)

if contador > 0 :
  print("El número no es primo" )
else:
  print("El nÚmero es primo")
def sueldo(cargo):
  dinero = 50
  if dinero == 50:
   print("Externo")
  elif dinero == 90:
   print("Ejecutivo")
  elif dinero == 100:
   print("Jefe")
   return dinero
