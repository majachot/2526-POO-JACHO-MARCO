class Habitacion:
    """
    Clase que representa una habitación de hotel.
    """
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def reservar(self):
        """Marca la habitación como no disponible"""
        if self.disponible:
            self.disponible = False
            return True
        return False

    def liberar(self):
        """Libera la habitación"""
        self.disponible = True


class Cliente:
    """
    Clase que representa un cliente del hotel.
    """
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni


class Reserva:
    """
    Clase que representa una reserva realizada por un cliente.
    """
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias

    def calcular_total(self):
        """Calcula el costo total de la reserva"""
        return self.habitacion.precio * self.dias


# ------------------ USO DEL SISTEMA ------------------

# Crear habitaciones
habitacion1 = Habitacion(101, "Simple", 50)
habitacion2 = Habitacion(102, "Doble", 80)

# Crear cliente
cliente1 = Cliente("Juan Pérez", "12345678")

# Realizar reserva
if habitacion1.reservar():
    reserva1 = Reserva(cliente1, habitacion1, 3)
    print("Reserva realizada con éxito")
    print(f"Cliente: {reserva1.cliente.nombre}")
    print(f"Habitación: {reserva1.habitacion.numero}")
    print(f"Total a pagar: ${reserva1.calcular_total()}")
else:
    print("La habitación no está disponible")