# Definición de la clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre  # Atributo público

    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito en las subclases")

# Definición de la clase derivada
class Perro(Animal):
    def hacer_sonido(self):
        return "Guauu!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miauu!"

# Ejemplo de encapsulación
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Fondos insuficientes")

    def obtener_saldo(self):
        return self.__saldo

# Creación de instancias y demostración de polimorfismo
animales = [Perro("Tarzan"), Gato("Mateo")]
for animal in animales:
    print(f"{animal.nombre} dice: {animal.hacer_sonido()}")

# Ejemplo de uso de la clase CuentaBancaria
cuenta = CuentaBancaria(200)
cuenta.depositar(100)
print(f"Saldo después del depósito: {cuenta.obtener_saldo()}")
cuenta.retirar(10)
print(f"Saldo después del retiro: {cuenta.obtener_saldo()}")
cuenta.retirar(130)  # Intento de retiro con fondos insuficientes
