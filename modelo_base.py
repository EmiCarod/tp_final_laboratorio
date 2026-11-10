from abc import ABC, abstractmethod

class CuentaBancaria(ABC):
    def __init__(self, numero_cuenta: str, titular: str, saldo_inicial: float = 0.0):
        self.__numero_cuenta = numero_cuenta
        self.__titular = titular
        self.__saldo = saldo_inicial

#getters y setters
    def get_numero_cuenta(self):
        return self.__numero_cuenta

    def get_titular(self):
        return self.__titular

    def get_saldo (self):
        return self.__saldo

    def set_saldo(self, nuevo_saldo: float):
        if nuevo_saldo >=0:
            self.__saldo = nuevo_saldo
        else:
            raise ValueError("El saldo no puede ser negativo")

    def depositar(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero")
        self.__saldo += monto

    @abstractmethod
    def retirar (self, monto: float):
        pass

class CajaAhorro(CuentaBancaria):
    def retirar(self, monto: float):
        if monto > self.get_saldo():
            raise ValueError ("Fondo insuficiente en la caja de ahorro")
        self.set_saldo (self.get_saldo() - monto)

class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta: str, titular: str, saldo_inicial: float = 0.0):
        super().__init__(numero_cuenta, titular, saldo_inicial)   

    def retirar(self, monto: float):
        self.set_saldo(self.get_saldo() - monto)