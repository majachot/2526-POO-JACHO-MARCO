class Tienda:
    def __init__(self, nombre):
        # Atributos
        self.nombre = nombre
        self.productos = {}  # Diccionario: producto -> precio

    def agregar_producto(self, producto, precio):
        self.productos[producto] = precio
        print(f"Producto '{producto}' agregado con precio ${precio}")

    def mostrar_productos(self):
        print(f"\nProductos disponibles en la tienda {self.nombre}:")
        for producto, precio in self.productos.items():
            print(f"- {producto}: ${precio}")

    def calcular_total(self, lista_compra):
        total = 0
        for producto in lista_compra:
            if producto in self.productos:
                total += self.productos[producto]
            else:
                print(f"El producto '{producto}' no existe en la tienda")
        return total


# Programa principal
tienda1 = Tienda("Tienda Central")

tienda1.agregar_producto("Arroz", 1.50)
tienda1.agregar_producto("Azúcar", 1.20)
tienda1.agregar_producto("Leche", 0.90)

tienda1.mostrar_productos()

compra = ["Arroz", "Leche"]
total = tienda1.calcular_total(compra)

print(f"\nTotal a pagar: ${total}")

class Farmacia:
    def __init__(self, nombre):
        # Atributos
        self.nombre = nombre
        self.medicamentos = {}  # Diccionario: medicamento -> [precio, stock]

    def agregar_medicamento(self, nombre_medicamento, precio, stock):
        self.medicamentos[nombre_medicamento] = [precio, stock]
        print(f"Medicamento '{nombre_medicamento}' agregado correctamente.")

    def mostrar_medicamentos(self):
        print(f"\nMedicamentos disponibles en la farmacia {self.nombre}:")
        for med, datos in self.medicamentos.items():
            precio, stock = datos
            print(f"- {med}: ${precio} | Stock: {stock}")

    def vender_medicamento(self, nombre_medicamento, cantidad):
        if nombre_medicamento in self.medicamentos:
            precio, stock = self.medicamentos[nombre_medicamento]
            if cantidad <= stock:
                total = precio * cantidad
                self.medicamentos[nombre_medicamento][1] -= cantidad
                print(f"Venta realizada: {cantidad} x {nombre_medicamento}")
                return total
            else:
                print("Stock insuficiente.")
        else:
            print("Medicamento no disponible.")
        return 0


# Programa principal
farmacia1 = Farmacia("Farmacia Cruz Azul")

farmacia1.agregar_medicamento("Paracetamol", 0.50, 100)
farmacia1.agregar_medicamento("Ibuprofeno", 0.80, 50)
farmacia1.agregar_medicamento("Vitamina C", 0.30, 80)

farmacia1.mostrar_medicamentos()

total_compra = farmacia1.vender_medicamento("Paracetamol", 5)
total_compra += farmacia1.vender_medicamento("Vitamina C", 3)

print(f"\nTotal a pagar: ${total_compra}")



