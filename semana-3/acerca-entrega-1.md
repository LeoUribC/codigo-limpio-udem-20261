# 🚩 Guía de la Primera Entrega (20%)

Esta entrega consiste en diseñar la base lógica de su proyecto de aula. El objetivo es construir una aplicación de terminal (CLI) que gestione un dominio específico, aplicando una separación de responsabilidades estricta.


## 💡 Ideas de proyectos

Pueden elegir uno de los siguientes temas o proponer uno similar para sus proyectos:

- Gestión de alquiler de películas.
- Reservas de vuelos o habitaciones de hotel.
- Control de inventario y ventas para un café.
- Sistema de préstamos de una biblioteca.

Como ven, son ideas de proyectos en donde se puedan efectuar operaciones CRUD con datos (crear, leer, actualizar y eliminar).

> [!IMPORTANT]
> En lo posible **no repetir temas de proyectos**, por lo cual los animo a que sean creativos!


## 📂 Estructura del proyecto (Clean "src" Layout)

Para cumplir con los criterios de Código Limpio, su repositorio debe seguir esta jerarquía:

```bash
nombre-del-proyecto/
├── data/
│   └── database.json         # Nuestra "Base de Datos" local
├── src/
│   └── mi_app/
│       ├── __init__.py
│       ├── cli.py            # Interfaz de usuario (Textual o Typer+Rich)
│       ├── models.py         # Definición de datos (Dataclasses)
│       ├── services.py       # Reglas de negocio (Lógica del CRUD)
│       ├── storage.py        # Capa de persistencia (Lectura/Escritura JSON)
│       └── exceptions.py     # Excepciones personalizadas
├── tests/                    # Pruebas unitarias con Pytest
├── .gitignore
├── pyproject.toml            # Configuración de uv y ruff
└── README.md                 # Documentación del proyecto
```


## 📋 Parámetros de calificación

1. Estándares de nomenclatura y estilo

- **Clases:** Uso de CamelCase (por ejemplo, `ReservaVuelo`).
- **Funciones y Variables:** Uso de snake_case (por ejemplo, `crear_reserva`).
- **Linter:** El código debe pasar la revisión de `ruff` sin advertencias.
- **Documentación:** Uso de Docstrings descriptivos en todas las clases y métodos públicos.
- **Tipado:** Uso estricto de Type Hinting (por ejemplo, `def buscar(id: int) -> Reserva:`).

2. Responsabilidad de las capas

- **Models:** Definiciones puras de datos usando `dataclasses`.
- **Storage:** Única capa autorizada para leer o escribir el archivo `.json` en la carpeta `data/`.
- **Services:** Aquí reside la "inteligencia", pues valida reglas (por ejemplo, "no alquilar si no hay stock") y coordina entre models y storage.
- **CLI:** Maneja la interacción con el usuario (por ejemplo, colores con `Rich`, comandos con `Typer`).

3. Calidad técnica

- **Excepciones:** No usar errores genéricos. Crear excepciones propias en `exceptions.py` (por ejemplo, `ElementoNoEncontradoError`).
- **Pruebas:** Al menos 10 casos de prueba (normales, extraordinarios y de error) ejecutados con `uv run pytest`, **todos deben pasar**.
- **Gestión:** Proyecto inicializado con `uv` y repositorio en GitHub con commits frecuentes.


## 📄 Contenido del README.md

Su archivo de presentación debe incluir:

- Explicación del proyecto, propósito y alcance.
- Guía de Instalación, instrucciones claras usando `uv`.
- Manual de la CLI; Ejemplos de comandos disponibles (por ejemplo, `uv run python -m mi_app.cli agregar --item "Pelicula A"`).
- Instrucciones de Testing: Cómo ejecutar las pruebas unitarias.
