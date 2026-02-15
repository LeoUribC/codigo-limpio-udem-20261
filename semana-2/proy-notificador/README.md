# 🧪 Laboratorio: Pruebas Unitarias y Arquitectura Profesional

En este proyecto, daremos el salto de "escribir scripts" a "construir sistemas", por lo cual aprenderemos a organizar nuestro código como lo hacen las grandes empresas tecnológicas y a implementar Pruebas Unitarias (Unit Testing) para garantizar que nuestro software sea robusto y confiable.

## 📂 Entendiendo la Estructura de Carpetas

En clase, vimos la siguiente estructura de carpetas sugerida:

```bash
mi-proyecto-aula/
├── .github/
│   └── workflows/          # CI/CD: Automatización de Pytest y Sphinx
├── docs/                   # Documentación generada con Sphinx
├── src/                    # Código fuente (Source)
│   └── mi_app/             # Paquete principal
│       ├── __init__.py
│       ├── interfaces.py   # Definición de Protocols (Clases Abstractas)
│       ├── modelos.py      # Lógica y entidades
│       └── cli.py          # Interfaz de Typer (para la CLI)
├── tests/                  # Pruebas Unitarias
│   ├── __init__.py
│   ├── test_modelos.py
│   └── test_logica.py
├── .gitignore
├── pyproject.toml          # Configuración de uv, dependencias y pytest
├── README.md               # Documentación principal
└── uv.lock                 # Versiones exactas de librerías
```

A esta estructura se le conoce como "src layout", y será utilizado a partir de ahora. Esta organización es un estándar en la industria por varias razones:

- `src/`: Aquí reside el código fuente real. Al estar dentro de una carpeta específica, evitamos que herramientas externas confundan archivos de configuración con lógica de la aplicación.

- `tests/`: Es el espejo de tu lógica. Por cada archivo en src, debe existir un archivo equivalente aquí para validar su funcionamiento.

- `pyproject.toml`: Es el cerebro del proyecto gestionado por uv. Aquí declaramos qué librerías necesitamos y cómo se configura nuestro entorno.


## 🧪 ¿Qué son las Pruebas Unitarias?

Una Prueba Unitaria es un pequeño fragmento de código que verifica una única "unidad" de trabajo (generalmente una función o un método) de forma aislada. Para entenderlo más fácil, piensa que estás haciendo un pastel, si lo preparas sin probar los ingredientes antes puede que salga mal y si eso ocurre no sabrás qué salió mal, pero si pruebas cada ingrediente antes de prepararlo y detectas algo raro en uno de ellos, podrás saber qué salió mal y corregirlo de inmediato. Cada ingrediente que pruebas es una prueba unitaria, y si cada prueba sale bien, entonces el pastel no tendrá problemas.

¿Por qué las usamos en Código Limpio?

Puedes cambiar el código interno; si los tests pasan, sabes que no rompiste nada. Además, un test te dice exactamente cómo se espera que se use una función, y si algo es difícil de probar, es porque el código está "sucio" o muy complejo de entender.


## 🏗️ Conceptos Avanzados de POO aplicados

En este proyecto, hemos implementado técnicas modernas para mejorar la calidad del código, tal y como es el uso de `Protocols`. En lugar de usar herencia rígida, usamos Protocolos, lo cual define un "contrato", indicando que cualquier clase que tenga un método `enviar(mensaje: str)` se considera un `Notificador`, siendo esto polimorfismo puro y flexible (conocido como *Static Duck Typing*). Además, observa cómo cada notificador valida sus propios datos (como el @ en el email) antes de actuar. Esto evita que los errores se propaguen por el sistema.


# 🚀 Ejecución y Testing con uv

Gracias a uv, el flujo de trabajo es extremadamente sencillo:

1. Ejecutar el programa:

```Bash
uv run src/notificador/logic.py
```

2. Ejecutar las Pruebas Unitarias:

Aquí es donde ocurre la magia, pytest buscará automáticamente todos los archivos que empiecen por `test_` y ejecutará las funciones de prueba.

```Bash
uv run pytest
```

**Pro tip:** Si quieres ver una salida detallada y colorida, intenta con `uv run pytest -v`.
