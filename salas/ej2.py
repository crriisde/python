print (" ")
print("Cristian David Salas De La O 3-W")
print (" ")
class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        """
        Constructor de la clase Cuenta.
        :param titular: Nombre del titular (obligatorio).
        :param cantidad: Cantidad inicial de dinero (opcional, por defecto 0.0).
        """
        self.__titular = titular
        self.__cantidad = float(cantidad)

    # Getters y setters
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, nuevo_titular):
        self.__titular = nuevo_titular

    @property
    def cantidad(self):
        return self.__cantidad

    # Métodos de la clase
    def mostrar(self):
        """Muestra los datos de la cuenta."""
        return f"Titular: {self.__titular}, Cantidad: {self.__cantidad:.2f}"

    def ingresar(self, cantidad):
        """
        Ingresa una cantidad a la cuenta. Si la cantidad es negativa, no se hace nada.
        :param cantidad: Cantidad a ingresar.
        """
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        """
        Retira una cantidad de la cuenta. Puede quedar en números rojos.
        :param cantidad: Cantidad a retirar.
        """
        self.__cantidad -= cantidad


# Uso de la clase
if __name__ == "__main__":
    # Crear una cuentaS
    cuenta = Cuenta("Juan Pérez")

    # Mostrar datos de la cuenta
    print(cuenta.mostrar())

    # Ingresar dinero
    cuenta.ingresar(500)
    print(cuenta.mostrar())

    # Retirar dinero
    cuenta.retirar(200)
    print(cuenta.mostrar())

    # Retirar más dinero (quedará en números rojos)
    cuenta.retirar(400)
    print(cuenta.mostrar())
