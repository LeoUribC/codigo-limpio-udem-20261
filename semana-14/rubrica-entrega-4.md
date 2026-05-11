# 🚀 Entrega 4 — Backend API con FastAPI

## 🎯 Objetivo

En esta entrega, cada equipo deberá construir la primera versión funcional del backend de su proyecto utilizando:

* FastAPI
* Supabase
* Arquitectura modular y limpia

El objetivo principal es implementar los **endpoints** necesarios para el funcionamiento de la aplicación.

---

## 📦 Alcance de la entrega

La evaluación estará enfocada exclusivamente en el backend (`api/`), en la correcta construcción de endpoints y en
el uso de los esquemas `pydantic` de una manera básica, por lo que no se evaluará todavía elementos como interfaz gráfica
completa, despliegue o frontend terminado.

---

## 🧱 Estructura esperada del proyecto

Se espera una estructura similar a la brindada en el proyecto `sample-fullapp` subido a uvirtual en la sección **RAE 3**.

---

## 📋 Requisitos mínimos

### API funcional con FastAPI

La aplicación debe:

* iniciar correctamente
* exponer endpoints funcionales
* utilizar routers organizados

Ejemplo esperado:

```bash
api/
    routers/
        users.py
        products.py
        orders.py
```

---

### Endpoints CRUD

Cada entidad principal del proyecto debe tener endpoints apropiados con los mínimos esperados:

| Método      | Operación  |
| ----------- | ---------- |
| GET         | Consultar  |
| POST        | Crear      |
| PUT / PATCH | Actualizar |
| DELETE      | Eliminar   |

---

### Uso de Pydantic Schemas

Los contratos de datos deben implementarse en:

```text
schemas/
```

Se evaluará:

* validación de datos
* tipado correcto
* separación entre request/response

---

### Separación de responsabilidades

Se espera una arquitectura limpia:

| Capa                 | Responsabilidad    |
| -------------------- | ------------------ |
| routers              | endpoints HTTP     |
| services             | lógica de negocio  |
| storage/repositories | acceso a Supabase  |
| schemas              | contratos de datos |

**Nota:** Únicamente validaré lo implementado en `api/` y `schemas/` de manera básica, lo demás deberá estar
implementado en la entrega final.

---

### Integración con Supabase

Los endpoints deben conectarse correctamente con Supabase, se evaluará:

* consultas funcionales
* organización del acceso a datos
* manejo básico de errores

---

### Variables de entorno

Las credenciales deben manejarse mediante

```text
.env
```

No deben existir credenciales hardcodeadas.

---

### Documentación automática

La API debe generar correctamente:

```bash
{url de localhost}/docs
```

y/o:

```bash
{url de localhost}/redoc
```

---

## 🧪 Evidencias requeridas

Cada grupo deberá entregar enlace al repositorio en donde el `README` tenga instrucciones de ejecución.

---

## 📊 Rúbrica de evaluación

| Criterio                            | Descripción                                         | Puntaje |
| ----------------------------------- | --------------------------------------------------- | ------- |
| **Estructura del proyecto**         | Organización modular y clara del backend            | 15 pts  |
| **Endpoints CRUD**                  | Endpoints completos y funcionales                   | 25 pts  |
| **Uso de FastAPI**                  | Correcto uso de routers, responses y tipado         | 15 pts  |
| **Schemas Pydantic**                | Validaciones, modelos request/response y type hints | 15 pts  |
| **Separación de responsabilidades** | Correcta división routers/services/storage          | 10 pts  |
| **Integración con Supabase**        | Conexión funcional y consultas correctas            | 10 pts  |
| **Variables de entorno**            | Uso adecuado de `.env` y seguridad básica           | 5 pts   |
| **Documentación automática**        | `{url localhost}/docs` funcional y clara            | 5 pts   |
