# Rúbrica de Calificación — Segunda Entrega del Proyecto

Esta rúbrica describe los criterios de evaluación para la **segunda entrega del proyecto del curso**.
El objetivo de esta fase es mejorar la calidad del proyecto mediante:

* refactorización del código
* documentación técnica profesional
* automatización de validaciones en CI
* mejores prácticas de diseño en Python

---

# 📊 Distribución de la calificación

| Criterio                                       | Peso |
| ---------------------------------------------- | ---- |
| Correcciones de la primera entrega             | 15%  |
| Documentación con MkDocs                       | 35%  |
| Refactorización y calidad del código           | 35%  |
| Mejora visual y pedagógica de la documentación | 15%  |

---

# Correcciones de la primera entrega (15%)

Cada equipo deberá **implementar las correcciones mencionadas en la retroalimentación de la primera entrega**.

Esto aplica únicamente para equipos que recibieron observaciones.

### Se evaluará:

* Corrección de errores señalados previamente
* Mejoras solicitadas en estructura del código
* Implementación de recomendaciones técnicas

| Nivel              | Descripción                                                |
| ------------------ | ---------------------------------------------------------- |
| Excelente (15 pts) | Todas las correcciones fueron implementadas correctamente. |
| Bueno (10 pts)     | La mayoría de las correcciones fueron aplicadas.           |
| Regular (5 pts)    | Algunas correcciones fueron aplicadas.                     |
| Deficiente (0 pts) | No se implementaron las correcciones.                      |

---

# Documentación con MkDocs y GitHub Pages (35%)

El proyecto debe incluir una **documentación técnica completa generada con MkDocs** y desplegada públicamente en **GitHub Pages**. Se recomienda utilizar el tema **Material for MkDocs**.

La documentación debe estar organizada con una estructura similar a la siguiente:

```
docs/
├── index.md
├── getting-started.md
├── user-guide/
│   ├── commands.md
│   └── persistence.md
├── architecture.md
└── reference.md
```

>Para que tengan una buena guía de cómo puede verse su documentación o qué incluir, les recomiendo que lean este link sobre [Diátaxis](https://diataxis.fr/start-here/).

> [!WARNING]
> Recuerden actualizar el elemento de `nav` en sus archivos de `mkdocs.yml` para que la estructura de páginas sea reconocida correctamente.

### Descripción de cada sección

**index.md:** Página de inicio del proyecto (landing page). Debe explicar:

* propósito del proyecto
* características principales
* arquitectura general

---

**getting-started.md:** Debe incluir:

* instalación usando `uv`
* sincronización de dependencias
* primer comando de la CLI

Ejemplo esperado:

```
uv sync
uv run main.py --help
```

---

**user-guide/commands.md:** Explica cómo usar la interfaz CLI. Debe incluir:

* ejemplos de comandos
* parámetros
* ejemplos de salida

---

**user-guide/persistence.md:** Explicación de cómo funciona la capa de persistencia:

* archivo JSON
* estructura de los datos
* cómo se serializan los modelos

---

**architecture.md:** Debe explicar decisiones de diseño:

* uso de `src layout`
* separación por capas
* principios de código limpio aplicados

---

**reference.md:** Aquí se debe integrar **documentación automática del código** usando `mkdocstrings`.

Esto debe incluir:

* modelos
* servicios
* storage

---

### Evaluación

| Nivel              | Descripción                                                                                  |
| ------------------ | -------------------------------------------------------------------------------------------- |
| Excelente (35 pts) | Documentación completa, clara, bien estructurada y desplegada correctamente en GitHub Pages. |
| Bueno (25 pts)     | Documentación funcional pero con secciones incompletas o poco detalladas.                    |
| Regular (15 pts)   | Documentación mínima o parcialmente implementada.                                            |
| Deficiente (0 pts) | No hay documentación o no está desplegada.                                                   |

---

# Refactorización y calidad del código (35%)

El proyecto debe demostrar mejoras en **estructura, organización y calidad del código**.

## Métrica obligatoria de complejidad

Se debe utilizar **Radon** para medir complejidad ciclomática.

Se evaluará:

```
uv run radon cc src -a
```

El proyecto debe tener una **calificación promedio final de A**.

---

## Integración en CI

La verificación de complejidad debe estar integrada en el workflow de pruebas. Ejemplo esperado en `tests.yml`:

```
- name: Check code complexity
  run: uv run radon cc src -a
```

Si el código supera el nivel permitido, el workflow debe fallar.

---

## Organización de modelos

Si el proyecto tiene múltiples entidades, los modelos deben organizarse en una carpeta:

```
src/app/models/
    user.py
    cart.py
    order.py
```

Cada entidad debe estar definida en **un archivo independiente**.

---

## Uso de dataclasses

Los modelos deben implementarse utilizando `dataclasses`.

Ejemplo esperado:

```
@dataclass
class User:
    id: int
    name: str
    email: str
```

---

## Validaciones en modelos

Las validaciones deben implementarse mediante:

```
__post_init__()
```

y métodos privados auxiliares.

Ejemplo:

```
def __post_init__(self):
    self._validate_email()
```

---

### Evaluación

| Nivel              | Descripción                                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------------ |
| Excelente (35 pts) | Código bien refactorizado, complejidad A, buena separación de módulos y modelos correctamente implementados. |
| Bueno (25 pts)     | Código funcional con algunas oportunidades de mejora estructural.                                            |
| Regular (15 pts)   | Código con problemas de organización o complejidad elevada.                                                  |
| Deficiente (0 pts) | Código sin refactorización o con estructura incorrecta.                                                      |

---

# Mejora visual y pedagógica de la documentación (15%)

Se incentiva a los equipos a enriquecer la documentación utilizando extensiones de Markdown disponibles en MkDocs.

### Pro Tips

Se recomienda el uso de:

**Admonitions**

Para destacar información importante:

```
!!! tip
    Este comando crea un usuario nuevo
```

---

**Tabs**

Para mostrar diferentes ejemplos:

```
=== "MacOS / Linux"

    uv sync

=== "Windows"

    uv sync
```

---

**Diagramas con Mermaid**

Para ilustrar arquitectura del sistema.

Ejemplo:

```
flowchart LR

CLI --> Service
Service --> Storage
Storage --> JSON
```

---

**Personalización visual**

Los equipos pueden mejorar la apariencia de la documentación:

* selección de paleta de colores
* iconos
* navegación clara
* diagramas explicativos

---

### Evaluación

| Nivel              | Descripción                                                                            |
| ------------------ | -------------------------------------------------------------------------------------- |
| Excelente (15 pts) | Documentación visualmente rica con admonitions, diagramas y buena organización visual. |
| Bueno (10 pts)     | Uso básico de herramientas de formato.                                                 |
| Regular (5 pts)    | Documentación simple sin enriquecimiento visual.                                       |
| Deficiente (0 pts) | Documentación mínima o inexistente.                                                    |

---

# 🎯 Objetivo de esta entrega

El propósito de esta fase es que los equipos aprendan a construir **proyectos con estándares cercanos a entornos profesionales**, incluyendo:

* documentación técnica clara
* código limpio y mantenible
* validación automática de calidad
* automatización mediante CI

---

# 🚀 Entrega

Cada equipo deberá entregar:

* repositorio actualizado en GitHub
* documentación desplegada en GitHub Pages
* workflows funcionando correctamente
* código refactorizado con complejidad promedio **A**

Pueden subir a la plataforma de uvirtual un archivo `.txt` con su link al repositorio y el nombre de los integrantes del equipo.

---
