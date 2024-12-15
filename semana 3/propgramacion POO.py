class Clima:
    def __init__(self):
        self.temperaturas = []
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    def ingresar_temperatura(self):
        for dia in self.dias:
            temp = float(input(f"Ingrese la temperatura para {dia}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    def mostrar_resultados(self):
        print("Temperaturas ingresadas:", self.temperaturas)
        print(f"El promedio de temperatura semanal es: {self.calcular_promedio():.2f}°C")

# Ejecución del programa
if __name__ == "__main__":
    clima = Clima()
    clima.ingresar_temperatura()
    clima.mostrar_resultados()
