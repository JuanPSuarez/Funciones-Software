# Trabajo Matematica Aplicada - 2do Año Tecnicatura Desarrollo de Software
# Integrantes: Metrebian Lucas, Suarez Juan Pablo

#Glosario: 
#   TermX = Término x
#   TermI = Término independiente
#   bPara = Término independiente con con aleatorio
#   aPerp = "A" Perpendicular
#   bPerp = "B" Perpendicular

#https://stackoverflow.com/questions/23344185/how-to-convert-a-decimal-number-into-fraction Decimales a Fracciones 
#https://github.com/nschloe/termplotlib ver para graficar
#https://www.geogebra.org/graphing?lang=en ver para graficar

from fractions import Fraction
import random
from math import sqrt

#-----------------------------------------------------------------------------
#Funciones
#-----------------------------------------------------------------------------

#Funcion para ecuacion lineal, paralela:
def linealParalela (termI): #El coeficiente principal se mantiene
    termI = random.randint(-50,50) #Termino independiente aleatorio
    return  termI

#Funcion para ecuacion lineal, prependicular:
def lineaPerpendicular(termX, termI):
    termX = -(termX**(-1)) #Inverso y negativo del coeficiente principal
    termI = random.randint(-50,50) #Termino independiente aleatorio
    return termX, termI



#FUNCIONES ANALISIS RECTA

#Corte con el Eje x.

def corteXlineal (termX, termI): 
    x = -(termI) / termX   #Se iguala funcion a 0.   #Se divide el coeficiente principal por el termino independiente.
    return x 



def corteYlineal (termX, termI):
    x = 0
    y = termX * (x) + termI
    return y


#Comportamiento de la recta.

def comportamientoRecta(a):
    if a > 0: # A = coeficiente principal
        comportamiento = "Creciente"
    else:
        comportamiento = "Decreciente"
    return comportamiento





# def encontrarPunt(a):
#     if find(.) in a:
#         a -> float

def excepcion (a):
    # while not a.isdigit():
    if a.find(".") >= 1:
        a=float(a)
    elif a.isnumeric():        
        a=float(a)
    else:
        a = input("Ha ingresado un caracter incorrecto. Ingrese solamente numeros: ")
        
    # while not a.isnumeric() and not type(a) == float:
    #     a = input("Ha ingresado un caracter incorrecto. Ingrese solamente numeros: ")
    # a = float(a)
    return a





#-----------------------------------------------------------------------------
#Menu Principal
#-----------------------------------------------------------------------------

OpMenu = int
while OpMenu != "0":
    OpMenu = input("""Ingrese una opcion: 
    1) Calcular Paralelas y Perpendicualres a una recta dada.
    2) Analisis de una ecuacion lineal.
    3) Analisis de ecuacion cuadratica.
    0) Salir.
    \n""")
    
    
#-----------------------------------------------------------------------------
#1) Recta paralela y Perpendicular a una dada.
#-----------------------------------------------------------------------------

#Input del usuario.
    if OpMenu == "1":
        
        a = 0
        while a == 0: #Evitamos que a == 0 pidiendole al usuario a =/= 0.
            a = input("Ingrese el termino de X: ")
            a = excepcion(a)
        b = input("Ingrese el termino independiente: ")
        b = excepcion(b)
        print("\n")
        print("La ecuacion es: " , a, "x +",b, "\n")

#Paralelas.
        contador = 0 #Variable que funciona de contador.
        while contador < 3: #Loop While va a correr 3 veces
            contador += 1
            bPara = linealParalela(b)
            print("Su ", contador, "° paralela es: ", a, "x +", bPara)
            
        contador = 1 #Volvemos a setear contador a 1.
        print("\n")

#Perpendiculares.
        contador = 0
        while contador < 3:
            contador += 1
            aPerp, bPerp = lineaPerpendicular(a, b)
            # aPerp = round(aPerp, 2)
            # aFracc = str(Fraction(aPerp))
            print ("Su", contador, "° perpendicular es " , aPerp, "x +", bPerp)
        print("\n")
        input("Presione una tecla para continuar.\n")
        
#-----------------------------------------------------------------------------
#2) Analisis de una recta.
#-----------------------------------------------------------------------------

#Input del usuario.
    if OpMenu == "2":
        a = 0 #Reusamos codigo de OpMenu == 1
        while a == 0: #Evitamos que a == 0 pidiendole al usuario a =/= 0.
            a = input("Ingrese el termino de X: ")
            a = excepcion(a)
        b = input("Ingrese el termino indepndiente: ")
        b = excepcion(b)
        print("\n")
        print("La ecuacion es: " , a, "x +",b)


#Corte con el Eje x.
        ejeX = corteXlineal(a,b)
        print("Coordenadas corte eje 'X': ", "(",ejeX,", 0 )")

#Corte con el Eje y.

        ejeY = corteYlineal(a,b)
        print("Coordenadas corte eje 'Y': ( 0,", ejeY,")," , "\n")


#Comportamiento de la recta.

        TipoRecta = comportamientoRecta(a)
        print("El comportamiento de la recta es:", TipoRecta, "\n")
        input("Presione una tecla para continuar.\n")

#-----------------------------------------------------------------------------
#3) Analisis de una parabola.
#-----------------------------------------------------------------------------

#Input del usuario.
    if OpMenu == "3":
        a = input("Ingrese coeficiente principal: ")
        a = excepcion(a)
        b = input("Ingrese termino x: ")
        b= excepcion(b)
        c = input("Ingrese el termino independiente: ")
        c = excepcion(c)
        print("\n")

        print("La ecuacion es: " , a, "x² +",b,"x +", c)

        basc=((b*b)-(4*a*c))
        ejeSim=-b/(2*a)
        vertice=((a*(ejeSim*ejeSim))+(b*ejeSim)+(c))
        xV=ejeSim
        yV=vertice
        concPar=""
        #Coordenadas al vertice.
        coorVer=(xV,yV)
        #Intervalo de crecimiento y decrecimiento.
        crece=("("+str(xV)+","+ "+∞ "+")")
        decre=("("+ "-∞"+","+ str(xV)+")")
        y=c

        if basc > 0:
#Corte con el Eje x.
            basc1=(-b+sqrt(((b*b)-(4*a*c))))/(2*a)
            #Corte con el Eje y.
            basc2=(-b-sqrt(((b*b)-(4*a*c))))/(2*a)
#Concavididad de la parabola.
            if a > 0:
                concPar= "Funcion Concava hacia Arriba"
            if a < 0:
                concPar= "Funcion Concava hacia Abajo"    
            print("El valor del discriminante: ", basc)
            print("La Ecuacion tiene solucion.")
            print("Corte en Eje x1 = "+str(basc1)) 
            print("Corte en Eje x2 = "+str(basc2))
            print("Corte en Eje Y = "+str(y))
            print("El eje de simetria es= " + str(ejeSim))
            print("El vertice es= " + str(vertice))
            print(concPar)
            print("Las coordenadas del vertice son = " + str(coorVer))
            print("La parabola crece en: " + str(crece))
            print("La parabola decrece en: "+str(decre))

#Doble multiplicidad.
        if basc == 0:
            print("La ecuacion tiene doble multiplicidad")
            print("Las coordenadas del vertice son = " + str(coorVer))
            print("El eje de simetria es= " + str(ejeSim))

#Parabola sin solucion.
        if basc < 0:
            print("No tiene solucion")
            print("Las coordenadas del vertice son = " + str(coorVer))
            print("El eje de simetria es= " + str(ejeSim))
        input("Presione una tecla para continuar.\n")

#1,0,1 no tiene solucion
#1,0,0 doble multiplicidad

#Agregar validaciones
#Agregar float en vez de int