import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from datetime import datetime


class AgendaPersonal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Agenda Personal")
        self.ventana.geometry("800x600")

        # Configurar frames contenedores
        self.frame_lista = tk.Frame(ventana)
        self.frame_entrada = tk.Frame(ventana)
        self.frame_botones = tk.Frame(ventana)

        # Componentes TreeView
        self.tree = ttk.Treeview(self.frame_lista, columns=('Fecha', 'Hora', 'Descripción'), show='headings')
        self.tree.heading('Fecha', text='Fecha')
        self.tree.heading('Hora', text='Hora')
        self.tree.heading('Descripción', text='Descripción')
        self.tree.pack(expand=True, fill='both')

        # Componentes de entrada de datos
        tk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5)
        self.calendario = Calendar(self.frame_entrada, date_pattern='dd/mm/yyyy')
        self.calendario.grid(row=0, column=1, padx=5)

        tk.Label(self.frame_entrada, text="Hora (HH:MM):").grid(row=1, column=0, padx=5)
        self.entrada_hora = tk.Entry(self.frame_entrada)
        self.entrada_hora.grid(row=1, column=1, padx=5)

        tk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5)
        self.entrada_desc = tk.Entry(self.frame_entrada, width=40)
        self.entrada_desc.grid(row=2, column=1, padx=5)

        # Botones de acción
        self.boton_agregar = tk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento)
        self.boton_eliminar = tk.Button(self.frame_botones, text="Eliminar Evento", command=self.eliminar_evento)
        self.boton_salir = tk.Button(self.frame_botones, text="Salir", command=ventana.quit)

        self.boton_agregar.pack(side=tk.LEFT, padx=5)
        self.boton_eliminar.pack(side=tk.LEFT, padx=5)
        self.boton_salir.pack(side=tk.LEFT, padx=5)

        # Organizar frames
        self.frame_lista.pack(fill='both', expand=True, padx=10, pady=10)
        self.frame_entrada.pack(fill='x', padx=10, pady=10)
        self.frame_botones.pack(fill='x', padx=10, pady=10)

    def validar_hora(self, hora):
        try:
            datetime.strptime(hora, "%H:%M")
            return True
        except ValueError:
            return False

    def agregar_evento(self):
        fecha = self.calendario.get_date()
        hora = self.entrada_hora.get()
        descripcion = self.entrada_desc.get()

        if not all([fecha, hora, descripcion]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        if not self.validar_hora(hora):
            messagebox.showerror("Error", "Formato de hora inválido (HH:MM)")
            return

        self.tree.insert('', 'end', values=(fecha, hora, descripcion))
        self.entrada_hora.delete(0, 'end')
        self.entrada_desc.delete(0, 'end')

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")
            return

        if messagebox.askyesno("Confirmar", "¿Eliminar el evento seleccionado?"):
            self.tree.delete(seleccionado)


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()
