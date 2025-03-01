import json
import os

class Inventario:
    def __init__(self, archivo='inventario.json'):
        self.productos = {}
        self.archivo = archivo
        self.cargar_inventario()  # Cargar inventario al iniciar

    def cargar_inventario(self):
        """Carga los productos desde el archivo de inventario."""
        if not os.path.exists(self.archivo):
            # Si el archivo no existe, lo crea vacío
            with open(self.archivo, 'w') as file:
                json.dump({}, file)
            print("Archivo de inventario creado.")

        try:
            with open(self.archivo, 'r') as file:
                datos = json.load(file)
                for id_producto, info in datos.items():
                    producto = Producto(id_producto, info['nombre'], info['cantidad'], info['precio'])
                    self.productos[id_producto] = producto
            print("Inventario cargado correctamente desde el archivo.")
        except FileNotFoundError:
            print("Error: El archivo no se encontró.")
        except PermissionError:
            print("Error: No se tienen permisos para leer el archivo.")
        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guarda los productos en el archivo de inventario."""
        datos = {}
        for id_producto, producto in self.productos.items():
            datos[id_producto] = {
                'nombre': producto.get_nombre(),
                'cantidad': producto.get_cantidad(),
                'precio': producto.get_precio()
            }

        try:
            with open(self.archivo, 'w') as file:
                json.dump(datos, file)
            print("Inventario guardado correctamente en el archivo.")
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        """Añade un nuevo producto al inventario y lo guarda en el archivo."""
        if producto.get_id() in self.productos:
            print("Error: El ID del producto ya existe. No se puede añadir.")
            return

        self.productos[producto.get_id()] = producto
        self.guardar_inventario()  # Guardar cambios en el archivo
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto por ID y actualiza el archivo."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()  # Guardar cambios en el archivo
            print("Producto eliminado correctamente.")
        else:
            print("Error: No se encontró el producto con el ID especificado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad o precio de un producto por ID y guarda los cambios."""
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            self.guardar_inventario()  # Guardar cambios en el archivo
            print("Producto actualizado correctamente.")
        else:
            print("Error: No se encontró el producto con el ID especificado.")

    def buscar_producto(self, nombre):
        """Busca productos por nombre y devuelve una lista de coincidencias."""
        resultados = []
        for producto in self.productos.values():
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
            return
        for producto in self.productos.values():
            print(producto)
