class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        # Verifica si el ID del producto ya existe en el inventario.
        for p in self.productos:
            if p.id_producto == producto.id_producto:
                print("Error: El ID del producto ya existe. No se puede añadir.")
                return  # Sale de la función si el ID ya existe

        self.productos.append(producto)  # Añade el producto si el ID es único
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        print("Producto eliminado correctamente.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.id_producto == id_producto:
                if cantidad is not None:
                    p.cantidad = cantidad
                if precio is not None:
                    p.precio = precio
                print("Producto actualizado correctamente.")
                return  # Importante: Sale de la función después de actualizar

        print("Error: No se encontró el producto con el ID especificado.")


    def buscar_producto(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.nombre.lower()]

    def mostrar_inventario(self):
        for producto in self.productos:
            print(producto)