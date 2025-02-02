import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        # Intentar leer el archivo con diferentes codificaciones
        try:
            with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
                print(f"\n--- Código de {ruta_script} (UTF-8) ---\n")
                print(archivo.read())
        except UnicodeDecodeError:
            print("Error al leer el archivo con codificación UTF-8. Intentando con Latin-1...")
            with open(ruta_script_absoluta, 'r', encoding='latin-1') as archivo:
                print(f"\n--- Código de {ruta_script} (Latin-1) ---\n")
                print(archivo.read())
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {e}")
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)
    opciones = {
        '1': 'calculadora area/calculadora_area.py',
        '2': 'Constructores y Destructores en Python/Constructores y Destructores en Python.py',
        '3': 'EjemploEncapsulacionHerencia/EjemploEncapsulacionHerencia.py',
        '4': 'EjemplosMundoReal_POO/bliblioteca.py',
        '5': 'semana dos/Unidad 1/1.2. Tecnicas de Programacion/1.2.1. Ejemplo Tecnicas de Programacion.py',
        '6': 'semana 3/programacion tradicional.py',
        '7': 'semana 3/propgramacion POO.py',
        # Agrega aquí el resto de las rutas de los scripts
    }
    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")
        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
