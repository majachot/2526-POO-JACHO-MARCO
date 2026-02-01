import os
import subprocess
import sys


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script_absoluta} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró:", ruta_script_absoluta)
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None


def ejecutar_codigo(ruta_script):
    try:
        # Usa el intérprete actual para ejecutar el script
        if os.name == 'nt':  # Windows
            # Abrir nueva ventana de cmd y ejecutar el script
            subprocess.Popen(['cmd', '/k', sys.executable, ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', sys.executable, ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")


def mostrar_menu():
    # Calcula la ruta raíz del proyecto (una carpeta arriba de 'Semana 08')
    ruta_actual = os.path.dirname(__file__)
    ruta_proyecto = os.path.dirname(ruta_actual)

    # Lista las carpetas dentro de la raíz del proyecto para adaptarse a tu repositorio
    try:
        carpetas = [f.name for f in os.scandir(ruta_proyecto) if f.is_dir()]
    except FileNotFoundError:
        print(f"La ruta del proyecto no existe: {ruta_proyecto}")
        return

    if not carpetas:
        print(f"No se encontraron carpetas en `{ruta_proyecto}`. Crea carpetas dentro del proyecto o mueve tus proyectos allí.")
        return

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú principal basadas en las carpetas encontradas
        for idx, carpeta in enumerate(carpetas, start=1):
            print(f"{idx} - {carpeta}")
        print("0 - Salir")

        eleccion = input("Elige una carpeta o '0' para salir: ").strip()
        if eleccion == '0':
            print("Saliendo del programa.")
            break
        try:
            opc = int(eleccion) - 1
            if 0 <= opc < len(carpetas):
                ruta_seleccionada = os.path.join(ruta_proyecto, carpetas[opc])
                mostrar_sub_menu(ruta_seleccionada)
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")
        except ValueError:
            print("Por favor ingresa un número válido.")


def mostrar_sub_menu(ruta_carpeta):
    # Lista subcarpetas y scripts .py dentro de la carpeta seleccionada
    try:
        entradas = list(os.scandir(ruta_carpeta))
    except FileNotFoundError:
        print(f"La carpeta no existe: {ruta_carpeta}")
        return

    sub_carpetas = [f.name for f in entradas if f.is_dir()]
    scripts_en_raiz = [f.name for f in entradas if f.is_file() and f.name.endswith('.py')]

    while True:
        print(f"\nContenido de: {ruta_carpeta}")
        opcion_num = 1
        opciones = []

        if sub_carpetas:
            print("Subcarpetas:")
            for s in sub_carpetas:
                print(f"{opcion_num} - {s} (carpeta)")
                opciones.append(('carpeta', s))
                opcion_num += 1

        if scripts_en_raiz:
            print("Scripts en esta carpeta:")
            for s in scripts_en_raiz:
                print(f"{opcion_num} - {s} (script)")
                opciones.append(('script', s))
                opcion_num += 1

        if not opciones:
            print("No hay subcarpetas ni scripts en esta carpeta.")
            input("Presiona Enter para regresar al menú principal.")
            return

        print("0 - Regresar al menú principal")

        eleccion = input("Elige una opción: ").strip()
        if eleccion == '0':
            return
        try:
            idx = int(eleccion) - 1
            if 0 <= idx < len(opciones):
                tipo, nombre = opciones[idx]
                ruta_seleccion = os.path.join(ruta_carpeta, nombre)
                if tipo == 'carpeta':
                    # Navegar a la subcarpeta
                    mostrar_sub_menu(ruta_seleccion)
                else:
                    # Mostrar y ofrecer ejecutar el script
                    codigo = mostrar_codigo(ruta_seleccion)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ").strip()
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_seleccion)
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print("Opción no válida. Regresando al menú de scripts.")
                        input("\nPresiona Enter para volver al menú.")
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")
        except ValueError:
            print("Por favor ingresa un número válido.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()