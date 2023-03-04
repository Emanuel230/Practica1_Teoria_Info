# Importamos librerias
import string
import math
from itertools import combinations
import re

# variable que tiene todas las mayusculas y el espacio.
alfabeto_es=(string.ascii_uppercase + " ")

# funcion que leera un texto y convertira todas su letras en mayusculas
def Leer_MostrarTxt(ar):
    #encoding="utf8" tipo de codificacion de mis archivos
    with open(ar,encoding="utf8") as f:
        caracter=f.read().upper()
    #retorna el texto en mayusculas 
    return caracter

# funcion para quitar el acento 
def QuitarAcento(x):
    # sabemos que en su mayoria los acentos estan en las vocales
    reemplazos = (("Á ", "A"),("É", "E"),("Í", "I"),("Ó", "O"),("Ú", "U"))
    #iteramos para que con la funcion replace() cuando encuentre vocales con tilde las reemplace
    for a, b in reemplazos:
        x = x.replace(a, b)
    # retornamos el texto sin las tildes
    return x
# funcion que limpia el texto(deja solo letras y el espacio)
def limpiando(e):
    # lista donde se guardaran los caracteres 
    lista =[]
    # iteramos en nuestro txt
    for i in e:
        # quitamos los saltos de linea
        if(i !="\n"):
            # isupper() devuelve true si es una letra en mayuscula
            # isspace() devuelve true si es un espacio
            if(i.isupper() or i.isspace()):
                # lo agregamos a la lista
                lista.append(i)
    # retornamos una lista con los unicos caracteres solicitados
    return lista

# funcion que cuenta las veces que aparece una letra en el txt 
def contador(d):
    ## iteramos en la variable de mayusculas y espacio
    for i in alfabeto_es:
        # con la funcion count() contamos cuantas letras hay (primero i es A y asi sucesivamente)
        contador=d.count(i)
        # imprimimos el caracter y enfrente el numero de veces que sale en el txt 
        print(i,contador)
# funcion que cuenta el numero de caracteres de el txt 
def numCaracter(e):
    # inicializamos contador
    contador=0
    #iteramos en el texto(e)
    for i in e:
        # filtramos los saltos de linea
        if(i != "\n"):
            # lo filtramos por mayusculas y espacios
            if(i.isalpha() or i.isspace()):
                # cada vez que cumpla estas condiciones se le suma 1 al contador
                contador+=1
    # retornamos el contador
    return contador

# funcion que calcula la probabilidad, informacion y entropia
def probabilidad_informacion_entropia(d):
    # inicializamos variable que guardara la entropia
    Entropia =0
    # asignamos a tam la longuitud de txt con la funcion len()
    tam=len(d)
    # iteramos en nuestro alfabeto(con el espacio)
    for i in alfabeto_es:
        # scamos la probabilidad contando cuantas veces sale i(nuestro caracter) y lo dividimos entre el tamaño
        probabilidad=((d.count(i)))/tam
        #imprimimos el caracter y enfrente su probabilidad y el %, reducimos que solo sean 8 decimales depues del punto
        print(i,"{0:.8f}".format(probabilidad),"%") 
        # sabemos que si la probabilida de un caracter es 0 nos daria error en la I(x)
        #por lo tanto le asignamos un 1 para que no nos afecte.
        if(probabilidad == 0):
            result=1
        # si no es 0 la probabilidad que a resultado le asigne el cociente del log de la info
        else:
            result=(1/probabilidad)
        # calculamos la informacion con la funcion log2()
        informacion=(math.log2(result))
        # imprimimos el caracter adelante la informacion y "Bits", reducimos que solo sean 8 decimales depues del punto
        print(i,"{0:.8f}".format(informacion),"Bits")
        # hace el producto de la probabilidad y la informacion que es la entropia
        re=probabilidad*informacion
        # Guardamos los valores de cada caracter 
        Entropia+=re
    #Imprimimos la suma total de re que sera la entropia
    print('H(x) :' , Entropia) 
    return Entropia

# Pares and tercias
#parejas= combinations(alfabeto_es,2)

# funcion que cuenta los pares de un texto
def contador_par(idioma):
    #creamos las combinaciones de mayusculas con espacios con la funcion combinations()
    parejas= combinations(alfabeto_es,2)
    # hacemos el cast de parejas , ahora sera de tipo list para que sea mejor iterar 
    par = list(parejas)
    # hacemos un cast ahora con el texto ya que la funcion que limpia nos regresa una lista
    txt4  = "".join(idioma) # cast a str
    #iteramos en la lista de parejas
    for i in par:
        # para el argumento de la funcion findall() 
        # hacemos el cast a str  (sabemos que par es list)
        x = "".join(i) # par que buscara 
        # con la funcion findall()  buscamos en todo el texto(segundo parametro)
        result = re.findall(x,txt4)
        # imprimimos el la pareja y enfrente con la funcion len() el "conteo"
        print(x,len(result))
# funcion para calcular la entropia de segundo orden
def entropiaH2(Entropia):
    print('2H(x) :',Entropia * 2)
# funcion oara calcular la entropia de 3 orden
def entropiaH3(Entropia):
    print('3H(x) :',Entropia * 3)
# funcion para calcular probabilidad y informacion de pares
def probabilidad_informacion_pares(d):
    # scacamos la longuitud dde nuestro txt
    tam=len(d)
    # realizamos las combninaciones
    parejas= combinations(alfabeto_es,2)
    # hacemos el casting a list para poder iterar mejor
    par = list(parejas)
    # hacemos el cast a str de nuestro txt
    f  = "".join(d)
    # iteramos en  nuestra lista par
    for i in par:
        # hacemos el cast de el valor de par a list
        x = "".join(i)
        # sacamos la probabilidad 
        probabilidad=((f.count(x)))/tam
        # imprimimos la probabilidad y reducimos su decimas a 8
        print(i,"{0:.8f}".format(probabilidad),"%") 
        # filtramos si la probabilidad es == 0 que le de a resultado 1 y asi no nos interfiere
        if(probabilidad == 0):
            result=1
        else:
            # si no que le de su valor
            result=(1/probabilidad)
        # calculamos la informacion con la formula
        informacion=(math.log2(result))
        # imprimimos y sacamos la informacion solo sus 8 decimas
        print(i,"{0:.8f}".format(informacion),"Bits")  

# funcion que cuenta las tercias en un texto
def contador_ter(idioma):
    # creamos las tercias como se hizo en pares(solo cambia el parametro de 2 a 3)
    tercias= combinations(alfabeto_es,3)
    # hacemos el cast a list para poder iterar
    ter = list(tercias)
    # hacemos el cast a str de el texto
    txt4  = "".join(idioma)
    # iteramos en la lista de tercias
    for i in ter:
        #hacemos el cast a str 
        x = "".join(i)
        # con la funcion findall() buscamos la tercias 
        # como parametro recibe x la tercia
        # y txt4 el texto donde buscara
        result = re.findall(x,txt4) # aqui se almacenan todas las tercias encontradas
        # imprimimos la tercia y despues la longuitud de result que sera la cantidad de veces de la tercia
        print(x,len(result))
# funcion que saca la probabilidad y informacion de tercias
def probabilidad_informacion_tercias(d):
    # tamaño del txt
    tam=len(d)
    # hacemos la combinaciones para tercias
    tercias= combinations(alfabeto_es,3)
    # hacemos el cast a lista de tercias para su iterracion
    ter = list(tercias)
    # hacemos el cast a str del txt
    f  = "".join(d)
    # iteramos en lista tercia
    for i in ter:
        # hacemos el cast de la tercia a str
        x = "".join(i)
        # sacamos la probabilidad de la tercia
        probabilidad=((f.count(x))*100)/tam
        # imprimimos la probabilidad con solo 8 num despues del punto
        print(i,"{0:.8f}".format(probabilidad),"%") 
        # filtramos la probabilidad para que no nos de error al momento de meterla en la formula de la informacion
        if(probabilidad == 0):
            result=1
        else:
            result=(1/probabilidad)
        # calculamos la informacion 
        informacion=(math.log2(result))
        # imprimimos la informacion
        print(i,"{0:.8f}".format(informacion),"Bits")  

# Menu para que el usuario al ejecutar el codigo pueda escoger
def menu():
    # se le pide al usuario escoger una opcion y se guarada en opc para que lo retorne la funcion
    # nos sirve en el while
    opc = int(input("******************************************\n" +
                    "*        Menu Principal                  *\n" +
                    "* 1. Seleccionar idioma del libro        *\n" +
                    "* 2. Frecuencia de caracteres            *\n" +
                    "* 3. P(x), I(x) , H(x)                   *\n" +
                    "* 4. Total de caracteres                 *\n" +
                    "* 5. Frecuencia de caracteres pares      *\n" +
                    "* 6. P(x), I(x) , H(x) pares             *\n" +
                    "* 7. Frecuencia de caracteres tercias    *\n" +
                    "* 8. P(x), I(x) , H(x) tercias           *\n" +
                    "* 9. Finalizar                           *\n" +
                    "******************************************\n" +
                    "Elija una Opcion :) \n")) 
    return opc
# inicializamos la opcion en 0
opcion = 0    

# Codigo principal
while opcion != 9:
    # se guarda la opcion que digito el usuario en el menu de inicio
    opcion = menu()
    # Opcion 1
    if opcion == 1:
        # se le pide al usuario que seleccione un idioma
        x = int(input("Seleccione el idioma del libro: 1 = Italiano  2 = Ingles  3 = Español\n"))
        # se igresa filtra la selecion del usuario
        if(x == 1):
            # leemos la opcion dicha 
            idioma=Leer_MostrarTxt('Romeo e Giulietta I.txt')
            # le mostramos un mensaje al usuario de varificacion de su eleccion
            print("Seleccionaste Italiano")

        # de igual manera para las otras dos opciones
        if(x==2):
            idioma=Leer_MostrarTxt('Romeo and Juliet E.txt')
            print("Seleccionaste Ingles")

        if(x==3):
            idioma=Leer_MostrarTxt('Romeo y Julieta S.txt')
            print("Seleccionaste Español")

        # por ultimo la ocion 1 limpia el texto conn la funciones dichas
        txt1 = QuitarAcento(idioma)
        txt2 = limpiando(txt1)
        # se le mande aun msj al usuario que se limpio correctamente
        print("Tu texto se a limpiado correctamente, solo queda el alfabeto y el espacio")
    # Opcion 2
    if opcion == 2:
        #Llamamos ala funcion contador la cual nos contara los caacteres de resultado de la eleccion en la opcion 1
        print("Frecuencia de caracteres ")
        contador(txt2)
    # Opcion 3
    if opcion == 3:

        entro=probabilidad_informacion_entropia(txt2)

    # Opcion 4   
    if opcion == 4:
        # Utiliza la funcion numCaracter() y regresa el total de caracteres en el libro
        tam = numCaracter(txt2)
        print("Total de caracteres es : ",tam)

    # Opcion 5   
    if opcion == 5:
        # Regresamos el conteo de los pares con la funcion ya dicha
        print("Frecuencia de caracteres pares ")
        contador_par(idioma)

    # Opcion 6   
    if opcion == 6:
        probabilidad_informacion_pares(txt2)
        entropiaH2(entro)

    # Opcion 7   
    if opcion == 7:
        # regresamos el conteo de tercias con la foncion ya vista
        print("Frecuencia de caracteres tercias ")
        contador_ter(idioma)

    # Opcion 8   
    if opcion == 8:
        probabilidad_informacion_tercias(txt2)
        entropiaH3(entro)

    # Opcion 9
    if opcion == 9:
        # termina el programa jejje    
        print("Programa terminado")
    # por si el usuario ingresa una opcion no valida
    if opcion > 9:
        print("opcion invalida") 
