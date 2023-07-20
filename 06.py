'''Investigue sobre el uso de la función list(), una vez comprendido su funcionamiento escriba un
programa que solicite al usuario una palabra y muestre por pantalla si es un palíndromo.'''


'''
# SIN HACER USO DE LA FUNCION LIST

palabra = input("\nIngrese una palabra a comprobar: ")

if palabra == palabra[::-1]:
    print("Es palindroma :D\n")
else:
    print("No es palindroma :(\n")
'''

# HACIENDO USO DE LA FUNCION LIST

palabra2 = []
p = None
i = 1

print("PRESIONE 1 Y ENTER PARA TERMINAR")

while p != 1:

    if p != '1':
        p = input(f"Ingrese letra #{i}: ")
        palabra2.append(p)
        i +=1
    else:
        palabra2.pop()
        break

print("\nEntonces tiene: ",palabra2)
arbalap = palabra2[:]
arbalap.reverse()
print("Que al reves seria: ",arbalap,"\n")

n = 0
for i in range(len(arbalap)):
    if arbalap[i] == palabra2[i]:
        n += 1
if len(palabra2) == n:
    print("Es palindroma")
else:
    print("No es palindroma")