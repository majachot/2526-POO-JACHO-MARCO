# Programacion Orientada a Objetos promedi semanal del clima
# Clase Base
class Clima:
    def __init__(self):
        self._temperaturas = []  # Atributo protegido (encapsulamiento)

    # Método para ingresar temperaturas (genérico)
    def ingresar_temperaturas(self, dias):
        for dia in range(1, dias + 1):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self._temperaturas.append(temp)

    # Método para calcular promedio
    def calcular_promedio(self):
        return sum(self._temperaturas) / len(self._temperaturas)


# Clase hija (hereda de Clima)
class ClimaSemanal(Clima):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase padre

    # Polimorfismo: se redefine el método
    def ingresar_temperaturas(self):
        print("Ingreso de temperaturas para la semana")
        super().ingresar_temperaturas(7)  # 7 días de la semana


# Programa principal
def main():
    print("=== Promedio Semanal del Clima (POO con Herencia) ===")

    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()

    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


# Ejecución del programa
main()