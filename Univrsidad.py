# Sistema de Gestión Universitaria 🎓

# Lista de estudiantes en la universidad
estudiantes = [
    {"id": 1, "nombre": "Carlos López", "cursos": [
        {"id": 101, "nombre": "Matemáticas", "notas": [85, 90, 78], "horario": "Lunes y Miércoles 10:00 - 12:00"},
        {"id": 102, "nombre": "Historia", "notas": [88, 92, 80], "horario": "Martes y Jueves 14:00 - 16:00"}
    ]},
    {"id": 2, "nombre": "Ana Torres", "cursos": [
        {"id": 101, "nombre": "Matemáticas", "notas": [75, 80, 70], "horario": "Lunes y Miércoles 10:00 - 12:00"},
        {"id": 103, "nombre": "Física", "notas": [90, 85, 88], "horario": "Viernes 08:00 - 10:00"}
    ]}
]

# Lista de cursos disponibles en la universidad
cursos = [
    {"id": 101, "nombre": "Matemáticas", "profesor": "Dr. Pérez", "estudiantes": [1, 2]},
    {"id": 102, "nombre": "Historia", "profesor": "Dra. Gómez", "estudiantes": [1]},
    {"id": 103, "nombre": "Física", "profesor": "Dr. Ramírez", "estudiantes": [2]}
]

# 📌 Agregar un nuevo estudiante y matricularlo en un curso
nuevo_estudiante = {"id": 3, "nombre": "Luis Mendoza", "cursos": []}
estudiantes.append(nuevo_estudiante)

# Matricular a Luis en Matemáticas
for curso in cursos:
    if curso["id"] == 101:
        curso["estudiantes"].append(3)
        nuevo_estudiante["cursos"].append({
            "id": 101,
            "nombre": "Matemáticas",
            "notas": [80, 85, 88],
            "horario": "Lunes y Miércoles 10:00 - 12:00"
        })
        break

# 📌 Calcular el promedio de notas de un estudiante
def calcular_promedio(id_estudiante):
    for estudiante in estudiantes:
        if estudiante["id"] == id_estudiante:
            total_notas = 0
            cantidad_notas = 0
            for curso in estudiante["cursos"]:
                total_notas += sum(curso["notas"])
                cantidad_notas += len(curso["notas"])
            return total_notas / cantidad_notas if cantidad_notas > 0 else 0

# Probando el cálculo de promedio para Carlos (ID 1)
promedio_carlos = calcular_promedio(1)

# 📌 Listar todos los estudiantes matriculados en un curso específico
def listar_estudiantes_curso(id_curso):
    for curso in cursos:
        if curso["id"] == id_curso:
            return [est["nombre"] for est in estudiantes if est["id"] in curso["estudiantes"]]

# Probando la función con Matemáticas (ID 101)
estudiantes_matematicas = listar_estudiantes_curso(101)

# Mostrando resultados 📊
print("Lista de estudiantes actualizada:")
for estudiante in estudiantes:
    print(f'ID: {estudiante["id"]}, Nombre: {estudiante["nombre"]}, Cursos: {[curso["nombre"] for curso in estudiante["cursos"]]}')

print("\nLista de cursos actualizada:")
for curso in cursos:
    print(f'ID: {curso["id"]}, Nombre: {curso["nombre"]}, Profesor: {curso["profesor"]}, Estudiantes: {curso["estudiantes"]}')

print(f"\nPromedio de notas de Carlos: {promedio_carlos:.2f}")

print("\nEstudiantes matriculados en Matemáticas:")
for estudiante in estudiantes_matematicas:
    print(estudiante)
