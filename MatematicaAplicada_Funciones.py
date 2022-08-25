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
    termI = random.randint(-100,100) #Termino independiente aleatorio
    return  termI

#Funcion para ecuacion lineal, prependicular:
def lineaPerpendicular(termX, termI):
    termX = -(termX**(-1)) #Inverso y negativo del coeficiente principal
    termI = random.randint(-100,100) #Termino independiente aleatorio
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




#FUNCIONES ANALISIS PARABOLA

#Corte con el Eje x.

#Corte con el Eje y.

#Intervalo de crecimiento y decrecimiento.

#Coordenadas al vertice.

#Concavididad de la parabola.

#Parabola sin solucion.

#Doble multiplicidad.



#-----------------------------------------------------------------------------
#Menu Principal
#-----------------------------------------------------------------------------

OpMenu = int
while OpMenu != 0:
    OpMenu = int(input("""Ingrese una opcion: 
    1) Calcular Paralelas y Perpendicualres a una recta dada.
    2) Analisis de una ecuacion lineal.
    3) Analisis de ecuacion cuadratica.
    0) Salir.
    \n"""))
    
    
#-----------------------------------------------------------------------------
#1) Recta paralela y Perpendicular a una dada.
#-----------------------------------------------------------------------------

#Input del usuario.
    if OpMenu == 1:
        
        a = 0
        while a == 0: #Evitamos que a == 0 pidiendole al usuario a =/= 0.
            a = int(input("Ingrese el termino de X: "))
        b = int(input("Ingrese el termino indepndiente: "))
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
        input("Presione una tecla para continuar.")

#-----------------------------------------------------------------------------
#2) Analisis de una recta.
#-----------------------------------------------------------------------------

#Input del usuario.
    if OpMenu == 2:
        a = 0 #Reusamos codigo de OpMenu == 1
        while a == 0: #Evitamos que a == 0 pidiendole al usuario a =/= 0.
            a = float(input("Ingrese el termino de X: "))
        b = float(input("Ingrese el termino indepndiente: "))
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
        input("Presione una tecla para continuar.")


#-----------------------------------------------------------------------------
#3) Analisis de una parabola.
#-----------------------------------------------------------------------------

#Input del usuario.
    if OpMenu == 3:
        a = float(input("Ingrese coeficiente principal: "))
        b = float(input("Ingrese termino x: "))
        c = float(input("Ingrese el termino independiente: "))
        print("\n")

        print("La ecuacion es: " , a, "x² +",b,"x +", c)

        basc=((b*b)-(4*a*c))
        ejeSim=-b/(2*a)
        vertice=((a*(ejeSim*ejeSim))+(b*ejeSim)+(c))
        xV=ejeSim
        yV=vertice
        concPar=""
        coorVer=(xV,yV)
        crece=("("+str(xV)+","+ "+∞ "+")")
        decre=("("+ "-∞"+","+ str(xV)+")")
        y=c

        if basc > 0:
            basc1=(-b+sqrt(((b*b)-(4*a*c))))/(2*a)
            basc2=(-b-sqrt(((b*b)-(4*a*c))))/(2*a)
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


        if basc == 0:
            print("doble multiplicidad")
        if basc < 0:
            print("no tiene solucion")

#Corte con el Eje x.

#Corte con el Eje y.

#Intervalo de crecimiento y decrecimiento.

#Coordenadas al vertice.

#Concavididad de la parabola.

#Parabola sin solucion.

#Doble multiplicidad.