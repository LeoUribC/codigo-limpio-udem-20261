from typing import Protocol
from rich.console import Console

console = Console()

# --- Interfaz (Protocolo) ---
class Notificador(Protocol):
    """Define el contrato que cualquier notificador debe seguir."""
    def enviar(self, mensaje: str) -> bool: ...

# --- Implementaciones (Polimorfismo) ---
class NotificadorEmail:
    def __init__(self, correo: str):
        self.correo = correo

    def enviar(self, mensaje: str) -> bool:
        if "@" not in self.correo:
            return False
        console.print(f"[blue]Enviando Email a {self.correo}:[/blue] {mensaje}")
        return True

class NotificadorSMS:
    def __init__(self, numero: str):
        self.numero = numero

    def enviar(self, mensaje: str) -> bool:
        if not self.numero.isdigit():
            return False
        console.print(f"[green]Enviando SMS al {self.numero}:[/green] {mensaje}")
        return True

# --- Lógica de Negocio (Uso de la Interfaz) ---
def difundir_alerta(mensaje: str, servicios: list[Notificador]) -> int:
    """Envía un mensaje a múltiples servicios y retorna cuántos fueron exitosos."""
    exitos = 0
    for servicio in servicios:
        if servicio.enviar(mensaje):
            exitos += 1
    return exitos