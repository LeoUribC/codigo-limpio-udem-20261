# Entrega 3 — Modelo Entidad-Relación y Base de Datos en Supabase

## Objetivo

En esta entrega, cada equipo deberá diseñar e implementar la **base de datos de su proyecto** utilizando PostgreSQL a través de Supabase.

El enfoque está en:

* Modelado correcto de datos (ER)
* Implementación en base de datos real
* Uso adecuado de restricciones e integridad

---

## Requisitos de la entrega

Cada equipo deberá entregar:

### Modelo Entidad-Relacióón (ER)

* Diagrama claro y legible
* Entidades correctamente definidas
* Relaciones bien establecidas
* Cardinalidades explícitas

📌 Formato sugerido:

* Imagen (PNG / JPG)
* Markdown con Mermaid
* PDF

Pueden apoyarse en recursos en línea como videos, tutoriales, documentación y otros recursos en distintos sitios web para
construir su diagrama de entidad relación, teniendo en cuenta las tablas de cada proyecto específico y sus referencias
mediante Primary Keys y Foreign Keys.

---

### Implementación en Supabase

La base de datos debe estar creada en Supabase e incluir:

#### ✔ Tablas correctamente definidas

* Uso de `PRIMARY KEY`
* Uso de `FOREIGN KEY`
* Tipos de datos adecuados

#### ✔ Restricciones

* `NOT NULL` donde aplique
* `UNIQUE` donde sea necesario
* Integridad referencial

#### ✔ Identificadores

* Uso de IDs autoincrementales (`SERIAL` o equivalente en donde aplique). Si por ejemplo definen un ID como una cédula de
ciudadanía, no es necesario que este valor sea autoincremental, puesto que cada cédula en sí misma es un identificador
único. Tengan casos así en cuenta para sus columnas de identificación única.

---

### Datos de prueba

Cada tabla debe contener **Mínimo 10 registros** y los datos deben ser coherentes con el modelo y relacionados
correctamente entre tablas.

---

## 🧪 Evidencias requeridas

El equipo deberá entregar:

* Diagrama ER
* Scripts SQL (opcional pero recomendado)
* Capturas de pantalla de:

  * Tablas creadas
  * Relaciones (FK)
  * Datos insertados

---

# 📊 Rúbrica de evaluación

| Criterio             | Descripción                                                    | Puntaje |
| -------------------- | -------------------------------------------------------------- | ------- |
| **Modelo ER**        | Diagrama claro, entidades bien definidas, relaciones correctas | 25 pts  |
| **Diseño de tablas** | Tablas bien estructuradas, tipos de datos adecuados            | 20 pts  |
| **Uso de claves**    | Correcto uso de PRIMARY KEY y FOREIGN KEY                      | 15 pts  |
| **Restricciones**    | Uso adecuado de NOT NULL, UNIQUE y consistencia de datos       | 15 pts  |
| **Datos de prueba**  | Mínimo 10 registros por tabla, coherencia en relaciones        | 15 pts  |
| **Presentación**     | Claridad en la entrega, organización y evidencias              | 10 pts  |

---

## ✅ Total: 100 puntos

---

# ⚠️ Observaciones importantes

* No se evaluará lógica de backend en esta entrega
* No es necesario integrar con Python todavía
* El enfoque es **modelado y base de datos**

---

# 💡 Recomendaciones

* Diseñar primero el modelo antes de crear tablas
* Validar relaciones antes de insertar datos
* Probar consultas simples (`SELECT`) para verificar consistencia

---

Muchos éxitos y Happy Coding!

