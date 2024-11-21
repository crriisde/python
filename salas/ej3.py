print (" ")
print("Cristian David Salas De La O 3-W")
print (" ")
class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        """
        Constructor de la clase Cuenta.
        :param titular: Diccionario con los datos del titular (nombre y edad).
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
        return f"Titular: {self.__titular['nombre']}, Edad: {self.__titular['edad']}, Cantidad: {self.__cantidad:.2f}"

    def ingresar(self, cantidad):
        """Ingresa una cantidad a la cuenta. Si la cantidad es negativa, no se hace nada."""
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        """Retira una cantidad de la cuenta. Puede quedar en números rojos."""
        self.__cantidad -= cantidad


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0):
        """
        Constructor de la clase CuentaJoven.
        :param titular: Diccionario con los datos del titular (nombre y edad).
        :param cantidad: Cantidad inicial de dinero (opcional, por defecto 0.0).
        :param bonificacion: Bonificación de la cuenta (en porcentaje, por defecto 0).
        """
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    # Getter y setter para bonificación
    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, nueva_bonificacion):
        self.__bonificacion = nueva_bonificacion

    # Métodos específicos de CuentaJoven
    def esTitularValido(self):
        """Devuelve True si el titular es mayor de edad pero menor de 25 años."""
        edad = self.titular['edad']
        return 18 <= edad < 25

    def mostrar(self):
        """Muestra los datos de la cuenta joven."""
        return f"Cuenta Joven\nTitular: {self.titular['nombre']}, Edad: {self.titular['edad']}, Cantidad: {self.cantidad:.2f}, Bonificación: {self.bonificacion}%"

    def retirar(self, cantidad):
        """Retira una cantidad de la cuenta sólo si el titular es válido."""
        if self.esTitularValido():
            super().retirar(cantidad)
        else:
            print("El titular no es válido para realizar esta operación.")
