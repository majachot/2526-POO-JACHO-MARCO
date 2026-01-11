# El programa esta diseñado para calcular el area de un triangulo,
# donde se puede observar los pasos a seguir en programacion que son el nombre de la clase,
# el metodo constructor con sus variables y adicional el calculo del area con la formula que corresponde
# base por altura sobre dos.

# Definición de la clase Triangulo
class Triangulo:
    # Método constructor que inicializa los atributos base y altura
    def __init__(self, base, altura):
        self.base = base           # Atributo que almacena la base del triángulo
        self.altura = altura       # Atributo que almacena la altura del triángulo

    # Método que calcula y devuelve el área del triángulo
    def calcular_area(self):
        # Fórmula del área del triángulo: (base * altura) / 2
        return (self.base * self.altura) / 2


# Programa principal

# Solicita al usuario que ingrese la base del triángulo
base = float(input("Ingrese la base del triángulo: "))

# Solicita al usuario que ingrese la altura del triángulo
altura = float(input("Ingrese la altura del triángulo: "))

# Se crea un objeto de la clase Triangulo con los valores ingresados
triangulo = Triangulo(base, altura)

# Se llama al método calcular_area para obtener el área del triángulo
area = triangulo.calcular_area()
# Se muestra el resultado del área en pantalla
print(f"El área del triángulo es: {area}")

