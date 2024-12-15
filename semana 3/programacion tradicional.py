# Definición de funciones

def ingresar_temperaturas():
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for dia in dias:
        temp = float(input(f"Ingrese la temperatura para {dia}: "))
        temperaturas.append(temp)

    return temperaturas


def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)


def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)

    print("Temperaturas ingresadas:", temperaturas)
    print(f"El promedio de temperatura semanal es: {promedio:.2f}°C")


# Ejecución del programa
if __name__ == "__main__":
    main()
