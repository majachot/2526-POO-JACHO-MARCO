from producto import Producto


class Inventario:
    """
    Clase que administra una lista de productos.
    """

    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        """
        Añade un producto asegurándose de que el ID sea único.
        """
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return False

        self.productos.append(producto)
        print("Producto añadido correctamente.")
        return True

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto por su ID.
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado correctamente.")
                return True

        print("Producto no encontrado.")
        return False

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto por ID.
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("Producto actualizado correctamente.")
                return True

        print("Producto no encontrado.")
        return False

    def buscar_por_nombre(self, nombre):
        """
        Busca productos por nombre (coincidencia parcial).
        """
        resultados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                resultados.append(p)

        return resultados

    def mostrar_todos(self):
        """
        Muestra todos los productos en el inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)