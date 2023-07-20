'''Escribir un programa que cree un diccionario vacío y lo vaya completando con información sobre
una persona (por ejemplo, nombre, edad, teléfono, correo electrónico, etc.) que se le solicite al
usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.'''


n = int(input("Cantidad de personas a ingresar: "))

perfil = {}
for _ in range(0,n):
    nombre = input("\nIngrese el nombre: ")
    edad = int(input("Ingrese edad: "))
    tel = int(input("Ingrese telefono: "))
    correo = input("Ingrese correo: ")

    perfil[nombre] = edad,tel,correo

print("\nDatos ingresados: \n")

for nombre in perfil:
    print("Nombre: ", nombre)
    print("Edad: ", edad)
    print("Telefono: ", tel)
    print("Correo: ", correo,"\n")