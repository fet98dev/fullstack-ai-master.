
'''
CUENTA BANCARIA
Crea una clase "CuentaBancaria" con atributos como número de cuenta y
saldo. Implementa métodos para depositar y retirar dinero, y muestra el
saldo actual.
'''

class cuentabancaria:
    def __init__(self, numero_cuenta="ES182938489", saldo=0):
        """Aniado atributos como numero de cuenta y saldo."""
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def depositar_dinero(self):
        """Esta funcion sirve para introducir dinero y sumarlo al saldo."""
        self.dinero = float(input("Ingresa dinero en la cuenta; "))
        self.saldo += self.dinero
        return self.saldo

    def retirar_dinero(self):
        """Esta funcion sirve para retirar dinero y restarlo del saldo"""
        self.dinero = float(input("Retira dinero en la cuenta; "))
        self.saldo -= self.dinero
        return self.saldo

    def muestra_saldo(self):
        """Esta funcion sirve para mostrar el saldo de la cuenta actualizado."""
        return (f"Saldo de la cuenta: {self.saldo}€")


mi_cuenta = cuentabancaria()
print(f"Has ingresado: {mi_cuenta.depositar_dinero()}")
print(f"Has retirado: {mi_cuenta.retirar_dinero()}")
print(mi_cuenta.muestra_saldo())

