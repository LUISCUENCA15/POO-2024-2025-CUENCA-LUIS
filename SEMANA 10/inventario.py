import os

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario()  # Cargar inventario al iniciar

    def cargar_inventario(self):
        """Carga los productos desde el archivo de inventario."""
        if not os.path.exists(self.archivo):
            # Si el archivo no existe, lo crea vacío
            open(self.archivo, 'w').close()
            print("Archivo de inventario creado.")

        try:
            with open(self.archivo, 'r') as file:
                for line in file:
                    id_producto, nombre, cantidad, precio = line.strip().split(',')
                    producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                    self.productos.append(producto)
            print("Inventario cargado correctamente desde el archivo.")
        except FileNotFoundError:
            print("Error: El archivo no se encontró.")
        except PermissionError:
            print("Error: No se tienen permisos para leer el archivo.")
        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guarda los productos en el archivo de inventario."""
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos:
                    file.write(f"{producto.id_producto},{producto.nombre},{producto.cantidad},{producto.precio}\n")
            print("Inventario guardado correctamente en el archivo.")
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        """Añade un nuevo producto al inventario y lo guarda en el archivo."""
        for p in self.productos:
            if p.id_producto == producto.id_producto:
                print("Error: El ID del producto ya existe. No se puede añadir.")
                return

        self.productos.append(producto)
        self.guardar_inventario()  # Guardar cambios en el archivo
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto por ID y actualiza el archivo."""
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        self.guardar_inventario()  # Guardar cambios en el archivo
        print("Producto eliminado correctamente.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad o precio de un producto por ID y guarda los cambios."""
        for p in self.productos:
            if p.id_producto == id_producto:
                if cantidad is not None:
                    p.cantidad = cantidad
                if precio is not None:
                    p.precio = precio
                self.guardar_inventario()  # Guardar cambios en el archivo
                print("Producto actualizado correctamente.")
                return

        print("Error: No se encontró el producto con el ID especificado.")

    def buscar_producto(self, nombre):
        """Busca productos por nombre y devuelve una lista de coincidencias."""
        return [p for p in self.productos if nombre.lower() in p.nombre.lower()]

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
            return
        for producto in self.productos:
            print(producto)
