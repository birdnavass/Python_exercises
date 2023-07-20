
from math import sqrt
 
def media(lista):
  s = 0
  for elemento in lista:
    s += elemento
  return s / float(len(lista))
 
def varianza(lista):
  s = 0
  m = media(lista)
  for elemento in lista:
    s += (elemento - m) ** 2
  return s / float(len(lista))
 
def desviacion_tipica(lista):
  return sqrt(varianza(lista))
 
lista=[1,2,3,4,5]
print(media(lista))
print(varianza(lista))
print(desviacion_tipica(lista))