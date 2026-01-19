# Clase base: Empleado
class Empleado:
    def __init__(self, nombre, salario):
        # Atributo público
        self.nombre = nombre

        # Atributo privado (encapsulación)
        self.__salario = salario

    # Método público para acceder al salario (getter)
    def get_salario(self):
        return self.__salario

    # Método público para modificar el salario (setter)
    def set_salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            print("El salario base debe ser mayor que 0")

    # Método que será sobrescrito (polimorfismo)
    def calcular_salario(self):
        return self.__salario

    def mostrar_info(self):
        print(f"Empleado: {self.nombre}, Salario: {self.calcular_salario()}")


# Clase derivada: EmpleadoTiempoCompleto (herencia)
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario, bono):
        # Llamada al constructor de la clase base
        super().__init__(nombre, salario)
        self.bono = bono

    # Polimorfismo: sobrescritura del método
    def calcular_salario(self):
        return self.get_salario() + self.bono

    def mostrar_info(self):
        print(
            f"Empleado Tiempo Completo: {self.nombre}, "
            f"Salario Total: {self.calcular_salario()}"
        )


# Programa principal
if __name__ == "__main__":
    # Crear una instancia de la clase base
    empleado1 = Empleado("Carla", 1000)
    empleado1.mostrar_info()

    # Modificar salario usando encapsulación
    empleado1.set_salario(1600)
    empleado1.mostrar_info()

n    # Crear una instancia de la clase derivada
    empleado2 = EmpleadoTiempoCompleto("Jose", 1100, 100)
    empleado2.mostrar_info()