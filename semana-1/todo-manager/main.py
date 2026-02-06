from datetime import datetime
# Importaciones de Rich para mejorar la salida en consola
from rich.console import Console
from rich.table import Table

console = Console()


class Tarea:
    """Clase que representa una entidad de Tarea"""
    
    def __init__(self, titulo: str, descripcion: str):
        self.titulo = titulo
        self.descripcion = descripcion
        self.__completada: bool = False  # Atributo privado
        self.fecha_creacion = datetime.now()

    def marcar_completada(self) -> None:
        """Cambia el estado de la tarea."""
        self.__completada = True

    @property  # el decorador @property convierte el método en un atributo de solo lectura
    def estado(self) -> str:
        """Getter temático para mostrar el estado de forma limpia."""
        return "Completada" if self.__completada else "⏳ Pendiente"


class GestorTareas:
    """Clase controladora que gestiona una colección de tareas (Composición)."""
    
    def __init__(self):
        # Inicializa una lista vacía de objetos tipo Tarea
        self.tareas: list[Tarea] = []

    def agregar_tarea(self, tarea: Tarea) -> None:
        self.tareas.append(tarea)
        console.print(f"[bold green]¡Éxito![/bold green] Tarea '{tarea.titulo}' añadida.")

    def mostrar_tablero(self) -> None:
        table = Table(title="📋 Mi Tablero de Código Limpio")
        table.add_column("Título", style="cyan")
        table.add_column("Estado", justify="center")
        table.add_column("Creada el", style="magenta")

        for tarea in self.tareas:
            table.add_row(tarea.titulo,
                          tarea.estado,
                          tarea.fecha_creacion.strftime("%Y-%m-%d %H:%M"))

        console.print(table)


# --- Punto de entrada del programa ---
if __name__ == "__main__":
    # Instanciación del gestor de tareas
    mi_gestor = GestorTareas()

    # Crear objetos de tarea
    tarea_calculo = Tarea("Tarea de algebra", "Tarea 1")
    tarea_fisica = Tarea("Tarea de campos", "Tarea 2")

    # Interactuar con los objetos
    mi_gestor.agregar_tarea(tarea_calculo)
    mi_gestor.agregar_tarea(tarea_fisica)

    # ya hicimos la tarea de calculo! La marcamos como completada
    tarea_calculo.marcar_completada()

    # Mostrar resultados
    mi_gestor.mostrar_tablero()
