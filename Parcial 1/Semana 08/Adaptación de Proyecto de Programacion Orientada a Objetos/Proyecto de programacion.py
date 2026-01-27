import os
import subprocess

# ============================================================
# CAMBIO 1:
# Se añadió el diccionario INFO para almacenar información
# académica organizada por materia y por sección
# (Evaluación, Tareas y Foros).
# En el código original NO existía esta estructura académica.
# ============================================================

INFO = {
    "Estadistica": {
        "Evaluacion": "Evaluación de Estadística: Análisis de datos, cálculo de media, mediana, moda y probabilidad básica.",
        "Tareas": "Ejercicios:\n1. Calcule la media y mediana del conjunto: 4, 6, 8, 10.\n2. Determine la probabilidad de obtener un número par al lanzar un dado.",
        "Foros": "Pregunta del foro: ¿Por qué la estadística es fundamental para el análisis de datos en Tecnologías de la Información?"
    },

    "Fisica": {
        "Evaluacion": "Evaluación de Física: Aplicación de las leyes de los gases ideales y conceptos básicos de energía.",
        "Tareas": "Ejercicios:\n1. Calcule el número de moles usando la ecuación PV=nRT.\n2. Identifique si un proceso es isotérmico o isocórico.",
        "Foros": "Pregunta del foro: ¿Cómo se aplican los principios de la física en los dispositivos tecnológicos actuales?"
    },

    "Matematicas": {
        "Evaluacion": "Evaluación de Matemáticas: Resolución de funciones y derivadas básicas.",
        "Tareas": "Ejercicios:\n1. Derive la función f(x)=5x².\n2. Resuelva la ecuación x² − 9 = 0.",
        "Foros": "Pregunta del foro: ¿Cómo ayudan las matemáticas a resolver problemas en programación y sistemas?"
    },

    "Programacion": {
        "Evaluacion": "Evaluación de Programación: Uso de Programación Orientada a Objetos y principios SOLID.",
        "Tareas": "Ejercicios:\n1. Cree una clase llamada Estudiante.\n2. Implemente un constructor y un método.",
        "Foros": "Pregunta del foro: ¿Por qué es importante aplicar buenas prácticas y escribir código limpio?"
    },

    "Sistemas": {
        "Evaluacion": "Evaluación de Sistemas: Conceptos de sistemas operativos, procesos y gestión de memoria.",
        "Tareas": "Ejercicios:\n1. Defina qué es un sistema operativo.\n2. Explique la diferencia entre proceso e hilo.",
        "Foros": "Pregunta del foro: ¿Qué papel cumple el sistema operativo en el rendimiento de una computadora?"
    }
}


# ============================================================
# CAMBIO 2:
# Se mantiene la función mostrar_codigo, pero ahora se usa
# para mostrar el contenido de scripts dentro de cada sección
# académica (tareas, evaluaciones, foros).
# ============================================================

def mostrar_codigo(ruta_script):
    try:
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            print("\n--- Código del script ---\n")
            print(archivo.read())
    except Exception as e:
        print(f"Error al leer el archivo: {e}")


# ============================================================
# CAMBIO 3:
# La función ejecutar_codigo se mantiene, pero ahora se
# ejecutan scripts asociados a materias académicas.
# ============================================================

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Error al ejecutar el script: {e}")


# ============================================================
# CAMBIO 4:
# El menú principal ahora representa un DASHBOARD ACADÉMICO
# para la carrera de Tecnologías de la Información.
# Se mantiene Unidad 1 y Unidad 2 del código original.
# ============================================================

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)
    unidades = {'1': 'Unidad 1', '2': 'Unidad 2'}

    while True:
        print("\n=== Carrera Tecnologías de la Información ===")
        for k, v in unidades.items():
            print(f"{k} - {v}")
        print("0 - Salir")

        op = input("Seleccione una unidad: ")
        if op == '0':
            break
        elif op in unidades:
            mostrar_materias(os.path.join(ruta_base, unidades[op]))


# ============================================================
# CAMBIO 5:
# Se reemplaza el submenú de carpetas genéricas
# por un menú fijo de MATERIAS ACADÉMICAS.
# ============================================================

def mostrar_materias(ruta_unidad):
    materias = list(INFO.keys())

    while True:
        print("\n--- Materias unidad seleccionada ---")
        for i, m in enumerate(materias, 1):
            print(f"{i} - {m}")
        print("0 - Regresar")

        op = input("Seleccione una materia: ")
        if op == '0':
            break
        try:
            materia = materias[int(op) - 1]
            mostrar_secciones(os.path.join(ruta_unidad, materia), materia)
        except:
            print("Opciones inválidas.")


# ============================================================
# CAMBIO 6:
# Se agregan secciones académicas:
# Evaluación, Tareas y Foros
# (en el código original solo había scripts).
# ============================================================

def mostrar_secciones(ruta_materia, materia):
    secciones = ["Evaluacion", "Tareas", "Foros"]

    while True:
        print("\n--- Secciones ---")
        for i, s in enumerate(secciones, 1):
            print(f"{i} - {s}")
        print("0 - Regresar")

        op = input("Seleccione una sección: ")
        if op == '0':
            break
        try:
            seccion = secciones[int(op) - 1]
            mostrar_info(materia, seccion)
            mostrar_scripts(os.path.join(ruta_materia, seccion))
        except:
            print("Opciones.")


# ============================================================
# CAMBIO 7:
# Nueva función que muestra información académica
# tomada del diccionario INFO.
# ESTA FUNCIÓN NO EXISTÍA EN EL CÓDIGO ORIGINAL.
# ============================================================

def mostrar_info(materia, seccion):
    print("\n=== Información Académica ===")
    print(f"Materia: {materia}")
    print(f"Sección: {seccion}")
    print(f"Descripción: {INFO[materia][seccion]}")
    print("============================\n")


# ============================================================
# CAMBIO 8:
# Se mantiene la lógica original de mostrar scripts,
# pero ahora los scripts están organizados por:
# Unidad → Materia → Sección
# ============================================================

def mostrar_scripts(ruta_seccion):
    scripts = [f for f in os.listdir(ruta_seccion) if f.endswith('.py')]

    if not scripts:
        print("No hay scripts disponibles en esta sección.")
        input("Presione Enter para continuar...")
        return

    while True:
        for i, s in enumerate(scripts, 1):
            print(f"{i} - {s}")
        print("0 - Regresar")

        op = input("Seleccione un script: ")
        if op == '0':
            break
        try:
            ruta_script = os.path.join(ruta_seccion, scripts[int(op) - 1])
            mostrar_codigo(ruta_script)
            if input("¿Ejecutar? (1=Sí / 0=No): ") == '1':
                ejecutar_codigo(ruta_script)
            input("Presione Enter para continuar...")
        except:
            print("Opción inválida.")


# ============================================================
# Punto de entrada principal (se mantiene igual)
# ============================================================

if __name__ == "__main__":
    mostrar_menu()
