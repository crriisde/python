
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        # Llamamos al constructor de la clase base (Cuenta)
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    # Getter y setter para el nuevo atributo
    def getBonificacion(self):
        return self.bonificacion

    def setBonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    # Método para verificar si el titular es válido (mayor de edad pero menor de 25 años)
    def esTitularValido(self):
        return 18 <= self.titular.edad < 25  # Asumiendo que el titular tiene un atributo edad

    # Modificamos la retirada de dinero para que solo sea posible si el titular es válido
    def retirarDinero(self, cantidad):
        if self.esTitularValido():
            if self.cantidad >= cantidad:
                self.cantidad -= cantidad
                return f"Has retirado {cantidad}€. Nuevo saldo: {self.cantidad}€"
            else:
                return "No tienes suficiente saldo para realizar la retirada."
        else:
            return "No puedes retirar dinero, ya que el titular no es válido."

    # Método mostrar para la cuenta joven
    def mostrar(self):
        return f"Cuenta Joven: Bonificación {self.bonificacion}% - Titular: {self.titular.nombre}, Saldo: {self.cantidad}€"
