import sqlite3

# Definir la conexión a la base de datos
def connect_db():
    """Crea una conexión con la base de datos SQLite"""
    conn = sqlite3.connect('tareas.db')  # 'tareas.db' es el archivo de la base de datos
    return conn

# Crear la tabla de tareas si no existe
def create_table():
    """Crea la tabla de tareas en la base de datos"""
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS tareas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT NOT NULL,
                        descripcion TEXT NOT NULL,
                        completada BOOLEAN NOT NULL)''')
    
    conn.commit()  # Guarda los cambios
    conn.close()   # Cierra la conexión

# Función para agregar una tarea
def add_tarea(titulo, descripcion):
    """Agrega una nueva tarea a la base de datos"""
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('''INSERT INTO tareas (titulo, descripcion, completada) 
                      VALUES (?, ?, ?)''', (titulo, descripcion, False))  # False indica que no está completada
    
    conn.commit()  # Guarda los cambios
    conn.close()   # Cierra la conexión

# Función para listar las tareas
def list_tareas():
    """Devuelve todas las tareas desde la base de datos"""
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM tareas')
    tareas = cursor.fetchall()  # Recupera todas las tareas
    conn.close()  # Cierra la conexión
    
    return tareas

# Función para marcar una tarea como completada
def mark_as_completed(tarea_id):
    """Marca una tarea como completada (True)"""
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('UPDATE tareas SET completada = ? WHERE id = ?', (True, tarea_id))
    
    conn.commit()  # Guarda los cambios
    conn.close()   # Cierra la conexión

# Función para eliminar una tarea
def delete_tarea(tarea_id):
    """Elimina una tarea de la base de datos"""
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM tareas WHERE id = ?', (tarea_id,))
    
    conn.commit()  # Guarda los cambios
    conn.close()   # Cierra la conexión
