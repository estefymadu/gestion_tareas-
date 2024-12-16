import json
from models import Tarea, Session

session = Session()

def agregar_tarea(titulo, descripcion):
    nueva_tarea = Tarea(titulo=titulo, descripcion=descripcion, completada=False)
    session.add(nueva_tarea)
    session.commit()
    print(f"Tarea '{titulo}' agregada.")

def listar_tareas():
    return session.query(Tarea).all()

def marcar_completada(id_tarea):
    tarea = session.query(Tarea).filter_by(id=id_tarea).first()
    if tarea:
        tarea.completada = True
        session.commit()
        print(f"Tarea '{tarea.titulo}' marcada como completada.")
    else:
        print(f"Tarea con id {id_tarea} no encontrada.")

def eliminar_tarea(id_tarea):
    tarea = session.query(Tarea).filter_by(id=id_tarea).first()
    if tarea:
        session.delete(tarea)
        session.commit()
        print(f"Tarea '{tarea.titulo}' eliminada.")
    else:
        print(f"Tarea con id {id_tarea} no encontrada.")


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

if __name__ == "__main__":
    # Llama a las funciones aquí para probarlas
    exportar_tareas()
    importar_tareas()