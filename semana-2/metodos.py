from abc import ABC, abstractmethod
from typing import final


class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self): ...

    @final
    def mensaje_transaccion(self) -> None:
        print("transaccion completada")


class PagoPaypal(MetodoPago):
    def __init__(self, email: str) -> None:
        self.email = email
   
    def procesar_pago(self, monto: float) -> None:
        print(f"pago con correo {self.email} hecho por ${monto}")


class PagoTarjeta(MetodoPago):
    def __init__(self, numero_tarjeta: str) -> None:
        self.numero_tarjeta = numero_tarjeta
   
    def procesar_pago(self, monto: float) -> None:
        print(f"pago con tarjeta {self.tarjeta} hecho por ${monto}")

class Procesador:
    def __init__(self, pagos: list[MetodoPago]) -> None:
        self.pagos = pagos
   
    def procesar_pagos(self):
        for pago in self.pagos:
            pago.mensaje_transaccion()


def main():
    paypal_1 = PagoPaypal("user@mail.com")
    tarjeta_1 = PagoTarjeta("1234-5678-9102")

    paypal_1.procesar_pago(100)
    paypal_1.mensaje_transaccion()

    procesador = Procesador([paypal_1, tarjeta_1])
    procesador.procesar_pagos()


if __name__ == "__main__":
    main()