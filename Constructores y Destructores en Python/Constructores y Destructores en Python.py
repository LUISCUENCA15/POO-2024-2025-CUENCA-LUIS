class Persona:
    def __init__(self, nombre, edad):
        # Constructor: inicializa los atributos del objeto
        self.nombre = nombre
        self.edad = edad
        print(f'Persona creada: {self.nombre}, Edad: {self.edad}')

    def __del__(self):
        # Destructor: se llama cuando el objeto es destruido
        print(f'El objeto Persona {self.nombre} ha sido destruido.')

    def presentarse(self):
        # Metodo para que la persona se presente
        print(f'Hola, mi nombre es {self.nombre} y tengo {self.edad} años.')

# Ejemplo de uso
persona_luis_Cuenca = Persona('Luis Cuenca', 36)  # Se crea un objeto de la clase Persona
persona_luis_Cuenca.presentarse()           # La persona se presenta
del persona_luis_Cuenca                      # Se fuerza la destrucción del objeto
