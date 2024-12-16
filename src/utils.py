import json
from models import Tarea, Session

session = Session()

def exportar_tareas(archivo="tareas.json"):
    tareas = session.query(Tarea).all()
    lista_tareas = [
        {"id": tarea.id, "titulo": tarea.titulo, "descripcion": tarea.descripcion, "completada": tarea.completada}
        for tarea in tareas
    ]
    with open(archivo, "w") as f:
        json.dump(lista_tareas, f, indent=4)
    print(f"Tareas exportadas a {archivo}.")

def importar_tareas(archivo="tareas.json"):
    try:
        with open(archivo, "r") as f:
            tareas_importadas = json.load(f)
        for t in tareas_importadas:
            tarea = Tarea(titulo=t["titulo"], descripcion=t["descripcion"], completada=t["completada"])
            session.add(tarea)
        session.commit()
        print("Tareas importadas correctamente.")
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe.")

