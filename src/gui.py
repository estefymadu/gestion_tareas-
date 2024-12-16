import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from PIL import Image, ImageTk

# Ruta del archivo de tareas
task_file = "tasks.json"

# Funcion para cargar tareas desde un archivo JSON
def load_tasks():
    if os.path.exists(task_file):
        with open(task_file, "r") as file:
            return json.load(file)
    return []

# Funcion para guardar tareas en un archivo JSON
def save_tasks():
    with open(task_file, "w") as file:
        json.dump(tasks, file)

# Funcion para iniciar sesion (solo ejemplo)
def login():
    email = email_entry.get()
    password = password_entry.get()
    if email and password:
        login_frame.pack_forget()
        task_frame.pack(fill='both', expand=True)
    else:
        error_label.config(text="Por favor ingrese sus datos correctamente")

def go_to_projects():
    project_tasks.clear()
    for task in tasks:
        if "(Completada)" not in task:
            project_tasks.append(task)
    update_project_list()
    task_frame.pack_forget()
    project_frame.pack(fill='both', expand=True)

def back_to_tasks():
    project_frame.pack_forget()
    task_frame.pack(fill='both', expand=True)

# Funcion para agregar una nueva tarea
def add_task():
    new_task = new_task_entry.get()
    if new_task:
        tasks.append(new_task)
        update_task_list()
        save_tasks()
        new_task_entry.delete(0, 'end')
    else:
        messagebox.showwarning("Input Error", "La tarea no puede estar vacía")

# Funcion para actualizar la lista de tareas
def update_task_list():
    for widget in task_list_frame.winfo_children():
        widget.destroy()
    for i, task in enumerate(tasks):
        task_frame_item = tk.Frame(task_list_frame, bg="#F9F9F9")
        task_frame_item.pack(fill="x", pady=2, padx=5)

        task_label = tk.Label(task_frame_item, text=task, bg="#F9F9F9", font=("Helvetica", 12))
        task_label.pack(side="left", padx=10)

        complete_button = ttk.Button(task_frame_item, text="✔", command=lambda idx=i: complete_task(idx))
        complete_button.pack(side="right")
        delete_button = ttk.Button(task_frame_item, text="❌", command=lambda idx=i: delete_task(idx))
        delete_button.pack(side="right", padx=5)

# Funcion para eliminar una tarea
def delete_task(index):
    del tasks[index]
    update_task_list()
    save_tasks()

# Funcion para marcar una tarea como completada
def complete_task(index):
    tasks[index] = tasks[index] + " (Completada)"
    update_task_list()
    save_tasks()

# Funcion para actualizar la lista de proyectos con tareas pendientes
def update_project_list():
    for widget in project_list_frame.winfo_children():
        widget.destroy()
    for task in project_tasks:
        project_label = tk.Label(project_list_frame, text=task, bg="#F0F0F0", font=("Helvetica", 12))
        project_label.pack(pady=5, anchor="w", padx=20)

# Ventana principal
root = tk.Tk()
root.title("Task Manager")
root.geometry("400x600")
root.configure(bg="white")

# Cargar tareas
tasks = load_tasks()
project_tasks = []

# Colores y estilos
button_style = {
    "background": "#4CAF50",
    "foreground": "white",
    "font": ("Helvetica", 10, "bold")
}

# ----- Login Frame -----
login_frame = tk.Frame(root, bg="white")
login_frame.pack(fill='both', expand=True)

title_label = tk.Label(login_frame, text="Task Manager", font=("Helvetica", 24, "bold"), bg="white", fg="#4CAF50")
title_label.pack(pady=20)

# Imagen decorativa
try:
    image = Image.open("task_icon.png").resize((100, 100))
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(login_frame, image=photo, bg="white")
    image_label.pack(pady=10)
except:
    pass

email_entry = ttk.Entry(login_frame, width=30)
email_entry.insert(0, "Email")
email_entry.pack(pady=10)

password_entry = ttk.Entry(login_frame, width=30, show="*")
password_entry.insert(0, "Password")
password_entry.pack(pady=10)

sign_in_button = tk.Button(login_frame, text="Sign In", **button_style, command=login)
sign_in_button.pack(pady=20)

error_label = tk.Label(login_frame, text="", fg="red", bg="white")
error_label.pack()

# ----- Task Frame -----
task_frame = tk.Frame(root, bg="white")

header_label = tk.Label(task_frame, text="Task List", font=("Helvetica", 20, "bold"), bg="#4CAF50", fg="white")
header_label.pack(fill="x", pady=10)

new_task_entry = ttk.Entry(task_frame, width=30)
new_task_entry.pack(pady=10, padx=10)

add_task_button = tk.Button(task_frame, text="Add Task", **button_style, command=add_task)
add_task_button.pack(pady=5)

task_list_frame = tk.Frame(task_frame, bg="white")
task_list_frame.pack(fill="both", expand=True, pady=10)

update_task_list()

project_button = tk.Button(task_frame, text="Go to Projects", **button_style, command=go_to_projects)
project_button.pack(pady=10)

# ----- Project Frame -----
project_frame = tk.Frame(root, bg="white")

project_title = tk.Label(project_frame, text="Projects (Pending Tasks)", font=("Helvetica", 20, "bold"), bg="#4CAF50", fg="white")
project_title.pack(fill="x", pady=10)

project_list_frame = tk.Frame(project_frame, bg="white")
project_list_frame.pack(fill="both", expand=True)

back_button = tk.Button(project_frame, text="Back to Tasks", **button_style, command=back_to_tasks)
back_button.pack(pady=20)

# Iniciar la aplicación
root.mainloop()

