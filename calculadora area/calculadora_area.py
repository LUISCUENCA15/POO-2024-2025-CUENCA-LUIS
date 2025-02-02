# Programa: Calculadora de área de un rectángulo
# Este programa solicita al usuario las dimensiones de un rectángulo (base y altura),
# calcula su área y muestra el resultado.

# Funciones
def calcular_area_rectangulo(base: float, altura: float) -> float:
    """Calcula el área de un rectángulo dada su base y altura.

    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.

    Returns:
        float: Área calculada del rectángulo.
    """
    return base * altura


# Solicitar datos al usuario
base = float(input("Introduce la base del rectángulo (en unidades): "))
altura = float(input("Introduce la altura del rectángulo (en unidades): "))

# Cálculo del área
area = calcular_area_rectangulo(base, altura)

# Mostrar el resultado
print(f"El área del rectángulo con base {base} y altura {altura} es: {area} unidades cuadradas.")
11