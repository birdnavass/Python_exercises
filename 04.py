'''Desarrolle un programa que almacene en una lista los números del 1 al 10 y los muestre por
pantalla en orden inverso separados por comas.'''


numeros = []

for _ in range(1,11):
    numeros.append(_)

print("\nNumeros: ",numeros)
numeros.reverse()
print("En reversa: ",numeros,"\n")