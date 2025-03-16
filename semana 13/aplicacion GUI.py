import tkinter as tk
from tkinter import ttk, messagebox


class AplicacionGUI:
    def __init__(self, ventana):
        # Configuración inicial de la ventana
        self.ventana = ventana
        self.ventana.title("Gestor de Tareas v1.0")
        self.ventana.geometry("500x400")
        self.ventana.resizable(False, False)

        # Variables de control
        self.lista_tareas = []

        # Creación de componentes
        self.crear_widgets()

    def crear_widgets(self):
        """Crea y posiciona todos los elementos en la ventana"""
        # Frame principal para organización
        main_frame = ttk.Frame(self.ventana, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Etiqueta de título
        lbl_titulo = ttk.Label(main_frame,
                               text="Ingrese nueva tarea:",
                               font=('Arial', 12, 'bold'))
        lbl_titulo.grid(row=0, column=0, sticky=tk.W, pady=5)

        # Campo de texto
        self.txt_tarea = ttk.Entry(main_frame, width=40)
        self.txt_tarea.grid(row=1, column=0, padx=5, pady=5)

        # Botones de acción
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=2, column=0, pady=10)

        self.btn_agregar = ttk.Button(btn_frame,
                                      text="Agregar Tarea",
                                      command=self.agregar_tarea)
        self.btn_agregar.pack(side=tk.LEFT, padx=5)

        self.btn_limpiar = ttk.Button(btn_frame,
                                      text="Limpiar Todo",
                                      command=self.limpiar_todo)
        self.btn_limpiar.pack(side=tk.LEFT, padx=5)

        # Lista de tareas
        self.lista = tk.Listbox(main_frame,
                                height=12,
                                selectmode=tk.SINGLE,
                                activestyle='none',
                                font=('Arial', 10))
        self.lista.grid(row=3, column=0, sticky=tk.NSEW, pady=10)

        # Scrollbar para la lista
        scrollbar = ttk.Scrollbar(main_frame,
                                  orient=tk.VERTICAL,
                                  command=self.lista.yview)
        scrollbar.grid(row=3, column=1, sticky=tk.NS)
        self.lista.config(yscrollcommand=scrollbar.set)

    def agregar_tarea(self):
        """Maneja el evento de agregar nueva tarea"""
        tarea = self.txt_tarea.get().strip()

        if tarea:
            self.lista_tareas.append(tarea)
            self.actualizar_lista()
            self.txt_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío",
                                   "Por favor ingrese una tarea válida")

    def limpiar_todo(self):
        """Limpia todos los elementos de la lista"""
        self.lista_tareas.clear()
        self.actualizar_lista()
        self.txt_tarea.delete(0, tk.END)

    def actualizar_lista(self):
        """Actualiza el Listbox con las tareas actuales"""
        self.lista.delete(0, tk.END)
        for idx, tarea in enumerate(self.lista_tareas, 1):
            self.lista.insert(tk.END, f"{idx}. {tarea}")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()
