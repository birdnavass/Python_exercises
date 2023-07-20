'''Escribir un programa que pregunte por una muestra de números, separados por comas, los
guarde en una lista y muestre por pantalla su media y desviación típica'''

from math import sqrt


n = int(input("\nIngrese el numero de muestras: "))

muestra = []
sum = 0

for i in range(0,n):

    temp = int(input(f"Ingrese la muestra #{i}: "))
    muestra.append(temp)
    sum = sum + temp

media = sum / len(muestra)

s = 0
j = 0

for j in muestra:
    s += (j - media) ** 2
var = s / float(len(muestra))

dm = sqrt(var)

print("\nLa media es: ", media)
print("La varianza es: ", var)
print("La desviacion tipica es: ",dm,"\n")