'''Cree un programa que almacene en una lista las asignaturas que esté cursando un estudiante
(por ejemplo, Matemáticas, Física, Química, Historia, Lenguaje, etc.) las cuales serán ingresadas
por el mismo dependiendo la cantidad que desee almacenar (por ejemplo, una materia, dos
materias, etc.); posteriormente haciendo uso de un bucle proceda a mostrar en pantalla el
mensaje "Yo estudio <asignatura>", donde <asignatura> es cada una de las asignaturas de la lista.'''


nomb = input("Escriba el nombre del alumno: ")
n = int(input("Cantidad d materias a ingresar: "))

materias = []

for _ in range(0,n):
    materia = input(f"Ingrese la #{_ + 1} materia: ")
    materias.append(materia)

print(f"\nYo {nomb} estudio: ")
print(materias,"\n")
