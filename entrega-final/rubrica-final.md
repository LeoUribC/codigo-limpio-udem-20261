# Entrega Final — Proyecto Fullstack

## Objetivo

La entrega final del curso tiene como propósito consolidar todos los conceptos trabajados durante el semestre, tales como Arquitectura limpia, Código limpio,, APIs REST con FastAPI, Bases de datos PostgreSQL con Supabase, Interfaces gráficas web, Automatización y calidad de software y documentación técnica.

Cada grupo deberá entregar una aplicación funcional fullstack siguiendo buenas prácticas de 
desarrollo profesional.

## Estructura esperada del proyecto

Se espera una organización similar a:

```bash
project/
├── pyproject.toml          # uv / dependencias
├── .env                    # SUPABASE_URL, SUPABASE_KEY
├── .env.example
├── README.md
│
├── src/
│   ├── api/                # FastAPI (backend)
│   │   ├── main.py         # App entrypoint, CORS, routers
│   │   ├── dependencies.py # Inyección de dependencias (DB client)
│   │   └── routers/
│   │       ├── users.py
│   │       ├── products.py
│   │       └── orders.py
│   │
│   ├── core/               # Configuración transversal
│   │   ├── config.py       # Settings con pydantic-settings (.env)
│   │   └── exceptions.py   # Excepciones de dominio
│   │
│   ├── schemas/            # Modelos Pydantic (contratos de datos)
│   │   ├── user.py
│   │   ├── product.py
│   │   └── order.py
│   │
│   ├── services/           # Lógica de negocio (orquestación)
│   │   ├── user_service.py
│   │   ├── product_service.py
│   │   └── order_service.py
│   │
│   ├── storage/            # Capa de acceso a datos (Supabase)
│   │   ├── base.py         # Clase base con manejo de errores
│   │   ├── user_repository.py
│   │   ├── product_repository.py
│   │   └── order_repository.py
│   │
│   └── app/                # Streamlit (frontend)
│       ├── main.py         # Entrypoint Streamlit
│       └── pages/
│           ├── users.py
│           ├── products.py
│           └── orders.py
│
└── tests/
    ├── conftest.py         # Fixtures, mocks de Supabase
    └── unit/
        ├── test_user_service.py
        ├── test_product_service.py
        └── test_order_service.py
```

---

## Requisitos de evaluación

### README del proyecto

El repositorio debe contener un `README.md` claro.

Debe incluir:

- descripción del proyecto
- instrucciones de instalación
- ejecución del backend
- ejecución del frontend
- variables de entorno necesarias
- tecnologías utilizadas
- estructura del proyecto

### Arquitectura y código limpio

Se evaluará:

1. Separación clara de capas con el uso correcto de:

| Capa                 | Responsabilidad               |
| -------------------- | ----------------------------- |
| api                  | endpoints HTTP                |
| services             | lógica de negocio             |
| storage/repositories | acceso a datos                |
| schemas              | contratos de datos (Pydantic) |
| core                 | configuración y excepciones   |

2. Uso de `src layout`, la estructura debe seguir el modelo trabajado en clase.
3. Excepciones personalizadas, uso apropiado de excepciones de dominio y manejo de errores.
4. Código limpio y se evaluará:
- nombres descriptivos
- funciones pequeñas
- ausencia de duplicación
- modularidad
- cohesión

### Automatización y calidad de software

El proyecto debe incluir workflows funcionales en GitHub Actions.

1. Pruebas unitarias, uso de pytest y mocks cuando aplique.
2. Ruff, validación automática de estilo y linting.
3. Radon, evaluación de complejidad ciclomática y se espera un promedio general mínimo de categoría A
4. Documentación automática con el uso de mkdocs, material for mkdocs y GitHub Pages (La documentación debe estar desplegada correctamente).

### Base de datos en Supabase

La aplicación debe utilizar PostgreSQL en Supabase y debe existir un modelo ER claro.

### Integridad de datos

Uso correcto de PRIMARY KEY, FOREIGN KEY, restricciones y relaciones

### Datos de prueba

La base de datos debe contener información suficiente para demostrar el funcionamiento de la aplicación.

---

## API REST con FastAPI

El backend debe contener endpoints funcionales.

### CRUD funcional

Los endpoints deben permitir:

- consultar    
- crear
- actualizar
- eliminar

### Validación de datos

Uso correcto de Pydantic schemas.

### Documentación automática

La API debe exponer correctamente:

```bash
/docs
/redoc
```

---

### Buenas prácticas

Se evaluará:

- routers organizados
- separación de responsabilidades
- status codes adecuados
- manejo de errores

---

## Interfaz gráfica web funcional

La aplicación debe incluir un frontend web funcional, se puede utilizar:

- Streamlit
- NiceGUI
- Cualquier herramienta front end con el que el estudiante tenga experiencia o sienta comodidad.

---

### Integración con backend

El frontend debe consumir correctamente los endpoints del backend.

---

### Flujo funcional completo

La interfaz debe permitir realizar operaciones reales sobre la base de datos.

---

### Usabilidad mínima

Se evaluará:

- navegación clara
- formularios funcionales
- visualización de datos

---

# Rúbrica de evaluación

|Criterio|Descripción|Puntaje|
|---|---|---|
|README y presentación del proyecto|Claridad, instrucciones y organización|10 pts|
|Arquitectura y código limpio|Separación de capas, modularidad y buenas prácticas|20 pts|
|Automatización y calidad|GitHub Actions, pytest, ruff, radon y documentación|20 pts|
|Base de datos y modelo ER|Diseño relacional y uso correcto de Supabase|15 pts|
|Backend FastAPI|Endpoints funcionales y arquitectura backend|20 pts|
|Frontend web funcional|Interfaz conectada correctamente al backend|15 pts|


Total: 100 puntos

---

## Penalizaciones

### Se penalizará:

- credenciales expuestas en el repositorio
- lógica de negocio dentro de routers
- código duplicado
- ausencia de separación de capas
- workflows rotos
- documentación inexistente
- endpoints no funcionales