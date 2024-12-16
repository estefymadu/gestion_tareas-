from controllers import agregar_tarea, listar_tareas, completar_tarea, eliminar_tarea, guardar_tareas, cargar_tareas
from models import init_db

def menu():
    while True:
        print("\n--- Aplicación de Gestión de Tareas ---")
        print("1. Agregar Tarea")
        print("2. Listar Tareas")
        print("3. Completar Tarea")
        print("4. Eliminar Tarea")
        print("5. Guardar Tareas")
        print("6. Cargar Tareas")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            titulo = input("Título: ")
            descripcion = input("Descripción: ")
            agregar_tarea(titulo, descripcion)
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            indice = int(input("Número de tarea a completar: "))
            completar_tarea(indice)
        elif opcion == "4":
            indice = int(input("Número de tarea a eliminar: "))
            eliminar_tarea(indice)
        elif opcion == "5":
            guardar_tareas()
        elif opcion == "6":
            cargar_tareas()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
            
from db import create_table

if __name__ == "__main__":
    create_table()  # Llamada para crear la tabla al inicio

