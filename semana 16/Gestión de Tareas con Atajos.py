import tkinter as tk
from tkinter import messagebox


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("600x400")

        # Configurar fuente y colores
        self.root.configure(bg="#F0F0F0")
        self.font_config = ("Arial", 12)

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(root, width=50, font=self.font_config)
        self.task_entry.pack(pady=15, padx=20)

        # Frame para botones
        button_frame = tk.Frame(root, bg="#F0F0F0")
        button_frame.pack(pady=10)

        # Botones de acción
        self.add_button = tk.Button(button_frame, text="Añadir Tarea (Enter)",
                                    command=self.add_task, bg="#4CAF50", fg="white")
        self.complete_button = tk.Button(button_frame, text="Completar (C)",
                                         command=self.mark_completed, bg="#2196F3", fg="white")
        self.delete_button = tk.Button(button_frame, text="Eliminar (D)",
                                       command=self.delete_task, bg="#F44336", fg="white")

        self.add_button.pack(side=tk.LEFT, padx=5)
        self.complete_button.pack(side=tk.LEFT, padx=5)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=60, height=15,
                                       font=self.font_config, selectbackground="#E0E0E0")
        self.task_listbox.pack(pady=15, padx=20)

        # Configurar atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<c>', lambda event: self.mark_completed())
        self.root.bind('<C>', lambda event: self.mark_completed())
        self.root.bind('<d>', lambda event: self.delete_task())
        self.root.bind('<D>', lambda event: self.delete_task())
        self.root.bind('<Escape>', lambda event: self.root.quit())

    def add_task(self):
        nueva_tarea = self.task_entry.get()
        if nueva_tarea:
            self.task_listbox.insert(tk.END, nueva_tarea)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "¡El campo de tarea no puede estar vacío!")

    def mark_completed(self):
        try:
            indice_seleccionado = self.task_listbox.curselection()[0]
            tarea = self.task_listbox.get(indice_seleccionado)
            if not tarea.startswith("[COMPLETADA]"):
                self.task_listbox.delete(indice_seleccionado)
                self.task_listbox.insert(indice_seleccionado, f"[COMPLETADA] {tarea}")
                self.task_listbox.itemconfig(indice_seleccionado, {'fg': '#757575'})
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea primero")

    def delete_task(self):
        try:
            indice_seleccionado = self.task_listbox.curselection()[0]
            self.task_listbox.delete(indice_seleccionado)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
