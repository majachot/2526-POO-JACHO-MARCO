class Persona:
    """
    Clase sencilla para demostrar el uso de constructor y destructor.
    """

    def __init__(self, nombre, edad):
        """
        Constructor de la clase.
        Se ejecuta automáticamente cuando se crea un objeto.

        Inicializa los atributos del objeto.
        """
        self.nombre = nombre
        self.edad = edad
        print(f"[INIT] Persona creada: {self.nombre}, {self.edad} años.")

    def saludar(self):
        """
        Método simple que muestra un saludo.
        """
        print(f"Hola, Ing. mi nombre es  {self.nombre} y tengo {self.edad} años.")

    def __del__(self):
        """
        Destructor de la clase.
        Se ejecuta cuando el objeto es eliminado o el programa finaliza.

        Se utiliza para realizar limpieza (en este caso, solo un mensaje).
        """
        print(f"[DEL] Persona eliminada: {self.nombre}.")


# -----------------------------
# Uso de la clase
# -----------------------------

if __name__ == "__main__":
    persona1 = Persona("Marco", 34)
    persona1.saludar()

    #Eliminamos el objeto para llamar al destructor
    del persona1

    print("Fin del programa.")