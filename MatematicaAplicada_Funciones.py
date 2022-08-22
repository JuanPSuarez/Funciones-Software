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

#Funcion para denotar el Comportamiento de la recta:
def comportamientoRecta(a):
    if a > 0: # A = coeficiente principal
        comportamiento = "Creciente"
    else:
        comportamiento = "Decreciente"
    return comportamiento

#-----------------------------------------------------------------------------
#Menu Principal
#-----------------------------------------------------------------------------
OpMenu = int
while OpMenu != 0:
    print ("""Ingrese una opcion: 
    1) Calcular Paralelas y Perpendicualres a una recta dada.
    2) Analisis de una ecuacion lineal.
    3) Analisis de ecuacion cuadratica.
    """)


#-----------------------------------------------------------------------------
#1) Recta paralela y Perpendicular a una dada.
#-----------------------------------------------------------------------------

#Input del usuario.
a = 0
while a == 0: #Evitamos que a == 0 pidiendole al usuario a =/= 0.
    a = int(input("Ingrese el termino de X: "))
b = int(input("Ingrese el termino indepndiente: "))
print("\n")

print("La ecuacion es: " , a, "x +",b)

#Paralelas.
contador = 0 #Variable que funciona de contador.
while contador < 3: #Loop While va a correr 3 veces
    contador += 1
    bPara = linealParalela(b)
    print("Su ", contador, "° paralela es: ", a, "x +", bPara)
    
contador = 1 #Volvemos a setear contador a 1.
print("\n")

#Perpendiculares.
while contador < 3:
    contador += 1
    aPerp, bPerp = lineaPerpendicular(a, b)
    # aPerp = round(aPerp, 2)
    # aFracc = str(Fraction(aPerp))
    print ("Su", contador, "° perpendicular es " , aPerp, "x +", bPerp)
print("\n")

#-----------------------------------------------------------------------------
#2) Analisis de una recta.
#-----------------------------------------------------------------------------

#Input del usuario.


#Corte con el Eje x.

#Corte con el Eje y.

#Comportamiento de la recta.

#-----------------------------------------------------------------------------
#3) Analisis de una parabola.
#-----------------------------------------------------------------------------

#Input del usuario.

#Corte con el Eje x.

#Corte con el Eje y.

#Intervalo de crecimiento y decrecimiento.

#Coordenadas al vertice.

#Concavididad de la parabola.

#Parabola sin solucion.

#Doble multiplicidad.