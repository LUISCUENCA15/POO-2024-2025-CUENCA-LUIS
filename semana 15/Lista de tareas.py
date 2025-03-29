import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Debe ingresar una tarea.")

def mark_completed():
    try:
        selected_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_index)
        listbox_tasks.delete(selected_index)
        listbox_tasks.insert(selected_index, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Aviso", "Seleccione una tarea para marcarla como completada.")

def delete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Aviso", "Seleccione una tarea para eliminarla.")

def on_enter(event):
    add_task()

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Entrada de texto
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=5)
entry_task.bind("<Return>", on_enter)

# Botones
btn_add = tk.Button(root, text="Añadir Tarea", command=add_task)
btn_add.pack(pady=2)
btn_complete = tk.Button(root, text="Marcar como Completada", command=mark_completed)
btn_complete.pack(pady=2)
btn_delete = tk.Button(root, text="Eliminar Tarea", command=delete_task)
btn_delete.pack(pady=2)

# Lista de tareas
listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
