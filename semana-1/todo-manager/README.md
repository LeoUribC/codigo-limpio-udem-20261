# Repaso de POO y Clean Code: Task Master CLI

¡Bienvenido a tu primer laboratorio! Este proyecto es un pequeño sistema de gestión de tareas diseñado para repasar los pilares de la **Programación Orientada a Objetos (POO)** mientras aplicamos estándares modernos de la industria.

## Cómo ejecutar este proyecto (La magia de `uv`)

Una de las ventajas de usar `uv` es que **no necesitas instalar manualmente las dependencias** ni activar entornos virtuales de la forma tradicional.

Para ejecutar el programa, simplemente sitúate en la carpeta del proyecto y corre:

```bash
uv run main.py
```

> **¿Qué acaba de pasar?** `uv` leyó el archivo `pyproject.toml`, identificó que el proyecto necesita la librería `rich`, creó un entorno aislado y ejecutó el código. Todo en milisegundos y sin ensuciar tu instalación global de Python.

---

## Puntos de Análisis (Reto para el Estudiante)

Mientras exploras el archivo `main.py`, presta atención a los siguientes conceptos que discutiremos en clase:

### 1. Nombres Significativos (Clean Code)

Observa que no usamos variables como `t`, `g` o `aux`. Los nombres como `Tarea`, `GestorTareas` y `marcar_completada` describen exactamente su propósito.

### 2. Type Hinting (Pistas de Tipo)

Fíjate en las anotaciones como `titulo: str` o `-> None`. Aunque Python es dinámico, el uso de tipos nos permite:

- Detectar errores antes de ejecutar el código.
- Mejorar el autocompletado en VS Code.
- Documentar qué espera cada función sin necesidad de comentarios excesivos.

### 3. Decoradores: `@property`

En la clase `Tarea`, usamos `@property` para el método `estado`. Esto permite acceder a `tarea.estado` como si fuera un atributo, pero ejecutando lógica interna para decidir qué emoji mostrar. Es una forma elegante de implementar _getters_ en Python.

### 4. Encapsulamiento y Privacidad

Nota el atributo `self.__completada`. El uso del doble guion bajo (`__`) es una convención de Python para proteger el estado interno. ¿Qué pasa si intentas modificarlo directamente desde fuera de la clase?

### 5. Composición de Clases

La clase `GestorTareas` contiene una lista de objetos de tipo `Tarea` (`list[Tarea]`). Esto es **composición**: un objeto "tiene" otros objetos para cumplir una responsabilidad mayor.

---

## 🚀 Desafío de Clase

Si ya lograste ejecutarlo, intenta modificar el código para:

1. Añadir un método en `GestorTareas` que permita eliminar una tarea por su título.
2. Agregar un nuevo atributo a la clase `Tarea` llamado `prioridad` (Alta, Media, Baja) y mostrarlo en la tabla.

