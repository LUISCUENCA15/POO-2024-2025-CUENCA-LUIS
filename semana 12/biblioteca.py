## 📚 Clase Libro
class Libro:
    """Representa un libro con atributos inmutables para título y autor."""

    def __init__(self, título: str, autor: str, categoría: str, isbn: str):
        self.datos_inmutables = (título, autor)  # Tupla inmutable (título, autor)
        self.categoría = categoría
        self.isbn = isbn

    def __repr__(self):
        return f"Libro: {self.datos_inmutables[0]} | Autor: {self.datos_inmutables[1]}"


## 👤 Clase Usuario
class Usuario:
    """Representa un usuario con capacidad para gestionar préstamos."""

    def __init__(self, nombre: str, id_usuario: str):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de objetos Libro

    def prestar_libro(self, libro: Libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro: Libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)


## 📖 Clase Biblioteca
class Biblioteca:
    """Sistema central que gestiona todos los recursos y operaciones."""

    def __init__(self):
        self.libros_disponibles = {}  # Dict {ISBN: Libro}
        self.usuarios_registrados = set()  # Set de IDs
        self.usuarios = {}  # Dict {ID: Usuario}
        self.préstamos = {}  # Dict {ID: [ISBNs]}

    # === Operaciones CRUD Libros ===
    def añadir_libro(self, libro: Libro):
        """Añade un libro al catálogo usando ISBN como clave única"""
        if libro.isbn in self.libros_disponibles:
            print("Error: ISBN ya existe")
            return
        self.libros_disponibles[libro.isbn] = libro

    def quitar_libro(self, isbn: str):
        """Elimina un libro por ISBN si existe y no está prestado"""
        if isbn not in self.libros_disponibles:
            print("ISBN no encontrado")
            return
        if any(isbn in prestamos for prestamos in self.préstamos.values()):
            print("No se puede eliminar: libro en préstamo")
            return
        del self.libros_disponibles[isbn]

    # === Gestión de Usuarios ===
    def registrar_usuario(self, usuario: Usuario):
        """Registra usuario verificando ID único"""
        if usuario.id_usuario in self.usuarios_registrados:
            print("Error: ID ya registrado")
            return
        self.usuarios_registrados.add(usuario.id_usuario)
        self.usuarios[usuario.id_usuario] = usuario

    def dar_de_baja_usuario(self, id_usuario: str):
        """Elimina usuario y gestiona préstamos activos"""
        if id_usuario not in self.usuarios_registrados:
            print("Usuario no encontrado")
            return
        if id_usuario in self.préstamos:
            print("Usuario tiene préstamos pendientes")
            return
        self.usuarios_registrados.remove(id_usuario)
        del self.usuarios[id_usuario]

    # === Operaciones Préstamos ===
    def prestar_libro(self, id_usuario: str, isbn: str):
        """Gestiona préstamos con verificaciones de estado"""
        if id_usuario not in self.usuarios_registrados:
            print("Usuario no registrado")
            return
        if isbn not in self.libros_disponibles:
            print("Libro no disponible")
            return
        if any(isbn in prestamos for prestamos in self.préstamos.values()):
            print("Libro ya prestado")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros_disponibles[isbn]
        usuario.prestar_libro(libro)
        self.préstamos.setdefault(id_usuario, []).append(isbn)

    def devolver_libro(self, id_usuario: str, isbn: str):
        """Gestiona devoluciones con validación de préstamo"""
        if id_usuario not in self.préstamos or isbn not in self.préstamos[id_usuario]:
            print("Préstamo no registrado")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros_disponibles[isbn]
        usuario.devolver_libro(libro)
        self.préstamos[id_usuario].remove(isbn)
        if not self.préstamos[id_usuario]:
            del self.préstamos[id_usuario]

    # === Búsquedas y Consultas ===
    def buscar_libros(self, keyword: str):
        """Búsqueda flexible por cualquier atributo del libro"""
        resultados = []
        kw = keyword.lower()
        for libro in self.libros_disponibles.values():
            if (kw in libro.datos_inmutables[0].lower() or  # Título
                    kw in libro.datos_inmutables[1].lower() or  # Autor
                    kw in libro.categoría.lower()):  # Categoría
                resultados.append(libro)
        return resultados

    def listar_préstamos_usuario(self, id_usuario: str):
        """Muestra libros prestados a un usuario específico"""
        if id_usuario not in self.usuarios:
            return []
        return self.usuarios[id_usuario].libros_prestados


# === Menú interactivo ===
def menu_biblioteca():
    biblioteca = Biblioteca()

    # Agregar algunos libros y usuarios para demostrar funcionalidades
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "978-8437604947")
    libro2 = Libro("1984", "George Orwell", "Ciencia ficción", "978-0451524935")
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)

    usuario1 = Usuario("Ana Torres", "A123")
    usuario2 = Usuario("Carlos Ruiz", "C456")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    while True:
        print("\n--- Menú de Biblioteca Digital ---")
        print("1. Añadir libro")
        print("2. Registrar usuario")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Buscar libros")
        print("6. Listar préstamos de un usuario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.añadir_libro(libro)
            print("¡Libro añadido!")

        elif opcion == "2":
            nombre = input("Nombre usuario: ")
            id_usuario = input("ID usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)
            print("¡Usuario registrado!")

        elif opcion == "3":
            id_usuario = input("ID usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "4":
            id_usuario = input("ID usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "5":
            keyword = input("Buscar (título/autor/categoría): ")
            resultados = biblioteca.buscar_libros(keyword)
            for libro in resultados:
                print(libro)

        elif opcion == "6":
            id_usuario = input("ID del usuario para ver préstamos: ")
            prestados = biblioteca.listar_préstamos_usuario(id_usuario)
            for libro in prestados:
                print(libro)

        elif opcion == "7":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu_biblioteca()

