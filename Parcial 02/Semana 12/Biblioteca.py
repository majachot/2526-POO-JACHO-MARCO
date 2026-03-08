import json

# -----------------------------
# Clases
# -----------------------------
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def to_dict(self):
        return {
            "titulo": self.info[0],
            "autor": self.info[1],
            "categoria": self.categoria,
            "isbn": self.isbn
        }

    @staticmethod
    def from_dict(data):
        return Libro(data["titulo"], data["autor"], data["categoria"], data["isbn"])

    def __str__(self):
        return f"Título: {self.info[0]}, Autor: {self.info[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "id_usuario": self.id_usuario,
            "libros_prestados": [libro.to_dict() for libro in self.libros_prestados]
        }

    @staticmethod
    def from_dict(data):
        usuario = Usuario(data["nombre"], data["id_usuario"])
        usuario.libros_prestados = [Libro.from_dict(libro) for libro in data.get("libros_prestados", [])]
        return usuario

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"


class Biblioteca:
    def __init__(self):
        self.libros = {}         # ISBN -> Libro
        self.usuarios = {}       # ID -> Usuario

    # -----------------------------
    # Añadir / quitar libros
    # -----------------------------
    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro '{libro.info[0]}' ya existe.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.info[0]}' agregado correctamente.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            libro = self.libros.pop(isbn)
            print(f"Libro '{libro.info[0]}' eliminado.")
        else:
            print("Libro no encontrado.")

    # -----------------------------
    # Registrar / dar de baja usuarios
    # -----------------------------
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            print("El ID de usuario ya existe.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado correctamente.")

    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios.pop(id_usuario)
            print(f"Usuario '{usuario.nombre}' eliminado.")
        else:
            print("Usuario no encontrado.")

    # -----------------------------
    # Prestar / devolver libros
    # -----------------------------
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return
        if isbn not in self.libros:
            print("Libro no disponible.")
            return
        usuario = self.usuarios[id_usuario]
        libro = self.libros.pop(isbn)
        usuario.libros_prestados.append(libro)
        print(f"Libro '{libro.info[0]}' prestado a {usuario.nombre}.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return
        usuario = self.usuarios[id_usuario]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros[isbn] = libro
                print(f"Libro '{libro.info[0]}' devuelto correctamente.")
                return
        print("El usuario no tiene este libro.")

    # -----------------------------
    # Guardar y cargar datos en JSON
    # -----------------------------
    def guardar_datos(self, archivo="biblioteca.json"):
        data = {
            "libros": [libro.to_dict() for libro in self.libros.values()],
            "usuarios": [usuario.to_dict() for usuario in self.usuarios.values()]
        }
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print("Datos guardados en archivo JSON.")

    def cargar_datos(self, archivo="biblioteca.json"):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.libros = {libro["isbn"]: Libro.from_dict(libro) for libro in data.get("libros", [])}
            self.usuarios = {usuario["id_usuario"]: Usuario.from_dict(usuario) for usuario in data.get("usuarios", [])}
            print("Datos cargados desde archivo JSON.")
        except FileNotFoundError:
            print("No se encontró el archivo JSON, iniciando con datos vacíos.")


# -----------------------------
# Ejemplo de uso con ingreso de datos por usuario
# -----------------------------
if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.cargar_datos()  # Cargar datos guardados previamente

    while True:
        print("\n--- Biblioteca Digital ---")
        print("1. Agregar libro")
        print("2. Registrar usuario")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Guardar datos y salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "3":
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "4":
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "5":
            biblioteca.guardar_datos()
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")
