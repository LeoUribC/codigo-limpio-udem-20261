# 🚀 Lenguajes de Programación y Código Limpio (2026-1)

¡Bienvenidos al curso! Este espacio está diseñado para transformar la forma en que escriben código, pasando de "simples scripts" a sistemas de software profesionales, mantenibles y elegantes.

Para este semestre, trabajaremos con herramientas de vanguardia que simulan un entorno de desarrollo profesional:

<details>
    <summary>🐧 Ecosistema Unix</summary>

mediante una de las siguientes opciones que se dejan libres al estudiante:
* [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) (Ubuntu) para un entorno Unix nativo en Windows. **Opción recomendada para la mayoría de estudiantes.**
* VirtualBox mediante la instalación de la ISO de Ubuntu en una máquina virtual.
* Instalación de Ubuntu en una partición del sistema y que se haga un dual boot.
* Si el estudiante dispone de un equipo con MacOS, puede hacer uso de este perfectamente.
</details>

<details>
    <summary>📖 Lenguaje</summary>

Python 3.12+ gestionado con [UV](https://docs.astral.sh/uv/), el gestor más rápido del ecosistema.
</details>

<details>
    <summary>⚙️ Lógica & CLI</summary>

[Typer](https://typer.tiangolo.com/) / [Textual](https://textual.textualize.io/) para interfaces de línea de comandos.
</details>

<details>
<summary>🌐 Web & API</summary>

[FastAPI](https://fastapi.tiangolo.com/) + [NiceGUI](https://nicegui.io/) / [Streamlit](https://streamlit.io/) para interfaces web modernas con puro Python.
</details>

<details>
<summary>📚 Persistencia</summary>

[Supabase](https://supabase.com/) (PostgreSQL cloud) + [SQLModel](https://sqlmodel.tiangolo.com/).
</details>

<details>
<summary>✅ Calidad</summary>

Pytest para pruebas y Ruff para linting.
</details>

<details>
<summary>⚙️ DevOps</summary>

GitHub Actions para CI/CD y Sphinx para documentación automatizada.
</details>



## 📅 Hitos de Evaluación (Proyecto de Aula)

| **Hito**      | **Descripción**                                                                          | **Peso** |
| ------------- | ---------------------------------------------------------------------------------------- | -------- |
| **Entrega 1** | CLI Robusta: Estructura de proyecto con `uv`, lógica en Typer/Textual y primeros tests.  | **20%**  |
| **Entrega 2** | Refactorización: Aplicación de Clean Code, manejo de excepciones y suite de Pytest.      | **15%**  |
| **Entrega 3** | Persistencia: Integración con Supabase y modelado de datos relacional.                   | **20%**  |
| **Entrega 4** | Capa Web: Migración a FastAPI, interfaz con NiceGUI y automatización con GitHub Actions. | **20%**  |
| **Final**     | Producto terminado: Documentación en Sphinx (GH Pages) y sustentación final.             | **25%**  |
