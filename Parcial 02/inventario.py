import json
import os
from producto import Producto


class Inventario:
    """
    Clase que administra una lista de productos
    y los almacena en un archivo JSON.
    """

    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    # ==============================
    # MÉTODOS DE ARCHIVO
    # ==============================

    def cargar_desde_archivo(self):
        """
        Carga los productos desde el archivo JSON.
        Si el archivo no existe, lo crea vacío.
        """
        try:
            if not os.path.exists(self.archivo):
                with open(self.archivo, "w") as f:
                    json.dump([], f)
                print("Archivo de inventario creado.")

            with open(self.archivo, "r") as f:
                datos = json.load(f)

                for item in datos:
                    producto = Producto(
                        item["id"],
                        item["nombre"],
                        item["cantidad"],
                        item["precio"]
                    )
                    self.productos.append(producto)

            print("Inventario cargado correctamente.")

        except json.JSONDecodeError:
            print("Error: El archivo está corrupto. Se iniciará vacío.")
            self.productos = []

        except PermissionError:
            print("Error: No hay permisos para leer el archivo.")

        except Exception as e:
            print(f"Error inesperado al cargar archivo: {e}")

    def guardar_en_archivo(self):
        """
        Guarda todos los productos en el archivo JSON.
        """
        try:
            datos = []

            for p in self.productos:
                datos.append({
                    "id": p.get_id(),
                    "nombre": p.get_nombre(),
                    "cantidad": p.get_cantidad(),
                    "precio": p.get_precio()
                })

            with open(self.archivo, "w") as f:
                json.dump(datos, f, indent=4)

            print("Cambios guardados en archivo correctamente.")

        except PermissionError:
            print("Error: No hay permisos para escribir en el archivo.")

        except Exception as e:
            print(f"Error inesperado al guardar archivo: {e}")

    # ==============================
    # MÉTODOS DE GESTIÓN
    # ==============================

    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return False

        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto añadido correctamente.")
        return True

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("Producto eliminado correctamente.")
                return True

        print("Producto no encontrado.")
        return False

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)

                self.guardar_en_archivo()
                print("Producto actualizado correctamente.")
                return True

        print("Producto no encontrado.")
        return False

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos
                if nombre.lower() in p.get_nombre().lower()]

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)