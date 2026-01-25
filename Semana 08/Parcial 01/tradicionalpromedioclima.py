# programacion Tradicional promedio semanal del clima
# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Programa principal
def main():
    print("=== Promedio Semanal del Clima (Programación Tradicional) ===")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")

# Ejecución del programa
main()