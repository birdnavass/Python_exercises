alumnos = []
cantidad = int(input("Ingrese cantidad a ingresar"))
contador = 0

while contador < cantidad:

    nombre = input("Ingrese nombre")
    apellido = input("Ingrese apellido")
    edad = input("Ingrese edad")
    email = input("Ingrese correo")

    informacion = {
        'nombre' : nombre,
        'apellido' : apellido,
        'edad' : edad,
        'email' : email,
    }

    alumnos.append(informacion)

    contador += 1

for alumno in alumnos:
    print("Nombre: ", alumno['nombre'],"\n")
    print("Apellido: ", alumno['apellido'],"\n")
    print("Edad: ", alumno['edad'],"\n")


#diccionario.values()
for info in alumno.values():
    print(info)

for info in alumno.items():
    print(info)