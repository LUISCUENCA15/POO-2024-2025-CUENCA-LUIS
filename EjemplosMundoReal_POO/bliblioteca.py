# Clase Libro que representa un libro en la biblioteca
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo  # Atributo: título del libro
        self.autor = autor    # Atributo: autor del libro
        self.disponible = True  # Atributo: estado de disponibilidad

    def prestar(self):
        """Método para prestar el libro."""
        if self.disponible:
            self.disponible = False
            print(f'El libro "{self.titulo}" ha sido prestado.')
        else:
            print(f'Lo siento, el libro "{self.titulo}" no está disponible.')

    def devolver(self):
        """Método para devolver el libro."""
        self.disponible = True
        print(f'El libro "{self.titulo}" ha sido devuelto.')


# Clase Usuario que representa un usuario de la biblioteca
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre  # Atributo: nombre del usuario

    def solicitar_prestamo(self, libro):
        """Método para solicitar el préstamo de un libro."""
        print(f'{self.nombre} está solicitando el préstamo del libro "{libro.titulo}".')
        libro.prestar()

    def devolver_libro(self, libro):
        """Método para devolver un libro."""
        print(f'{self.nombre} está devolviendo el libro "{libro.titulo}".')
        libro.devolver()


# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancias de libros
    libro1 = Libro("1984", "George Orwell")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry")

    # Crear una instancia de usuario
    usuario1 = Usuario("Luis Cuenca")

    # Solicitar préstamo y devolver libros
    usuario1.solicitar_prestamo(libro1)  # Luis solicita "1984"
    usuario1.solicitar_prestamo(libro1)  # Luis intenta solicitar "1984" nuevamente
    usuario1.devolver_libro(libro1)      # Luis devuelve "1984"
    usuario1.solicitar_prestamo(libro2)  # Luis solicita "El Principito"
