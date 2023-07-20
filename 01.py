'''Desarrolle un programa que solicite al usuario un número entero positivo y en una lista proceda
a almacenarlo todos los números impares desde 1 hasta el número ingresado, posteriormente
muestre el resultado de la lista en pantalla.'''


n = int(input("\nCantidad a ingresar: "))

impares = []

for _ in range(0,n):
    ingreso = int(input(f"Ingrese numero #{_ + 1}: "))
    if ingreso % 2 == 0 and ingreso >= 0:
        impares.append(ingreso)

print("\n",impares,"\n")