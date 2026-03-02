import json  # Permite trabajar con archivos en formato JSON (serialización)
import os    # Permite verificar si un archivo existe en el sistema


# =====================================================
# CLASE PRODUCTO
# Representa un producto individual del inventario
# =====================================================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        Se ejecuta automáticamente cuando se crea un nuevo objeto Producto.
        """

        # Atributos privados (convención con _)
        # Representan las características del producto
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # -----------------------------
    # MÉTODOS GETTERS
    # Permiten obtener los valores
    # -----------------------------

    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # -----------------------------
    # MÉTODOS SETTERS
    # Permiten modificar los valores
    # -----------------------------

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    # ---------------------------------------------------
    # Método para convertir el objeto en diccionario
    # Esto es necesario para poder guardarlo en JSON
    # ---------------------------------------------------
    def to_dict(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

    # ---------------------------------------------------
    # Método especial para mostrar el producto en texto
    # ---------------------------------------------------
    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"


# =====================================================
# CLASE INVENTARIO
# Administra todos los productos usando un diccionario
# =====================================================
class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa la colección donde se almacenarán los productos.
        """

        # Diccionario para almacenar productos
        # Clave (key): ID del producto
        # Valor (value): Objeto Producto
        # Esto permite búsqueda rápida en tiempo O(1)
        self.productos = {}

    # ---------------------------------------------------
    # MÉTODO PARA AGREGAR UN NUEVO PRODUCTO
    # ---------------------------------------------------
    def agregar_producto(self, producto):
        # Verifica si el ID ya existe en el diccionario
        if producto.get_id() in self.productos:
            print("❌ Error: El producto ya existe.")
        else:
            # Se añade el producto al diccionario
            self.productos[producto.get_id()] = producto
            print("✅ Producto agregado correctamente.")

    # ---------------------------------------------------
    # MÉTODO PARA ELIMINAR UN PRODUCTO POR SU ID
    # ---------------------------------------------------
    def eliminar_producto(self, id_producto):
        # Se verifica si el ID existe
        if id_producto in self.productos:
            # Se elimina usando la palabra clave del
            del self.productos[id_producto]
            print("✅ Producto eliminado.")
        else:
            print("❌ Producto no encontrado.")

    # ---------------------------------------------------
    # MÉTODO PARA ACTUALIZAR CANTIDAD O PRECIO
    # ---------------------------------------------------
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):

        # Se verifica si el producto existe
        if id_producto in self.productos:

            # Solo se actualiza si el usuario ingresó un nuevo valor
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)

            if precio is not None:
                self.productos[id_producto].set_precio(precio)

            print("✅ Producto actualizado.")
        else:
            print("❌ Producto no encontrado.")

    # ---------------------------------------------------
    # MÉTODO PARA BUSCAR PRODUCTOS POR NOMBRE
    # Utiliza comprensión de listas
    # ---------------------------------------------------
    def buscar_por_nombre(self, nombre):

        # Se recorre el diccionario y se filtran coincidencias
        encontrados = [
            producto for producto in self.productos.values()
            if nombre.lower() in producto.get_nombre().lower()
        ]

        # Si se encontraron productos, se muestran
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("❌ No se encontraron productos.")

    # ---------------------------------------------------
    # MÉTODO PARA MOSTRAR TODOS LOS PRODUCTOS
    # ---------------------------------------------------
    def mostrar_todos(self):

        # Si el diccionario no está vacío
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("📦 Inventario vacío.")

    # ---------------------------------------------------
    # MÉTODO PARA GUARDAR EL INVENTARIO EN UN ARCHIVO
    # Serialización usando JSON
    # ---------------------------------------------------
    def guardar_en_archivo(self, nombre_archivo="inventario.json"):

        # Se convierte cada objeto Producto en diccionario
        datos = {
            id_prod: prod.to_dict()
            for id_prod, prod in self.productos.items()
        }

        # Se abre el archivo en modo escritura
        with open(nombre_archivo, "w") as archivo:
            json.dump(datos, archivo, indent=4)

        print("💾 Inventario guardado correctamente.")

    # ---------------------------------------------------
    # MÉTODO PARA CARGAR EL INVENTARIO DESDE ARCHIVO
    # Deserialización desde JSON
    # ---------------------------------------------------
    def cargar_desde_archivo(self, nombre_archivo="inventario.json"):

        # Verifica si el archivo existe antes de intentar abrirlo
        if os.path.exists(nombre_archivo):

            # Se abre el archivo en modo lectura
            with open(nombre_archivo, "r") as archivo:
                datos = json.load(archivo)

                # Se reconstruyen los objetos Producto
                for id_prod, prod_data in datos.items():
                    producto = Producto(
                        prod_data["id"],
                        prod_data["nombre"],
                        prod_data["cantidad"],
                        prod_data["precio"]
                    )

                    # Se vuelve a insertar en el diccionario
                    self.productos[id_prod] = producto

            print("📂 Inventario cargado correctamente.")
        else:
            print("⚠ No existe archivo previo. Inventario iniciado vacío.")


# =====================================================
# FUNCIÓN MENÚ (INTERFAZ DE USUARIO)
# =====================================================
def menu():

    # Se crea una instancia del inventario
    inventario = Inventario()

    # Se intenta cargar información previa
    inventario.cargar_desde_archivo()

    # Bucle infinito hasta que el usuario decida salir
    while True:

        print("\n====== SISTEMA DE INVENTARIO ======")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        # -----------------------------
        # OPCIÓN 1: AGREGAR
        # -----------------------------
        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        # -----------------------------
        # OPCIÓN 2: ELIMINAR
        # -----------------------------
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        # -----------------------------
        # OPCIÓN 3: ACTUALIZAR
        # -----------------------------
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")

            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")

            # Si el usuario deja vacío, no se actualiza ese campo
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        # -----------------------------
        # OPCIÓN 4: BUSCAR
        # -----------------------------
        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        # -----------------------------
        # OPCIÓN 5: MOSTRAR TODOS
        # -----------------------------
        elif opcion == "5":
            inventario.mostrar_todos()

        # -----------------------------
        # OPCIÓN 6: GUARDAR
        # -----------------------------
        elif opcion == "6":
            inventario.guardar_en_archivo()

        # -----------------------------
        # OPCIÓN 7: SALIR
        # -----------------------------
        elif opcion == "7":
            # Se guarda automáticamente antes de salir
            inventario.guardar_en_archivo()
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida.")


# Punto de entrada del programa
# Esto garantiza que el menú solo se ejecute
# si el archivo se ejecuta directamente
if __name__ == "__main__":
    menu()