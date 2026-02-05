# 🛠️ Configuración del Entorno: De la Terminal al Primer Proyecto

Esta guía asume que ya has habilitado **WSL2** en tu sistema. Si no lo has hecho, el primer paso es seguir la documentación oficial.

## 1. Preparación de WSL (Windows Subsystem for Linux)

Antes de continuar, asegúrate de tener instalada una distribución de Linux (recomendamos **Ubuntu 22.04 LTS** o superior).

- [Guía de Instalación oficial de Microsoft](https://learn.microsoft.com/en-us/windows/wsl/install)


> **⚠️ Importante:** Todos los comandos que verás a continuación **DEBEN** ser ejecutados dentro de tu terminal de Ubuntu (la ventana negra de Linux), **no** en el PowerShell ni en el CMD de Windows.

---

## 2. Instalación de Git

Git es esencial para el control de versiones y es un requisito para que `uv` gestione algunas dependencias. En tu terminal de Ubuntu, ejecuta:

```Bash
sudo apt update
sudo apt install git -y
```

>*Puedes verificar la instalación con `git --version`.*

---

## 3. Instalación de `uv`

`uv` será nuestro gestor de paquetes y versiones de Python. Es extremadamente rápido y eficiente.

1. **Instalador:**

```Bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. **Configuración del entorno:** Para que el comando `uv` funcione de inmediato, reinicia la terminal:

---

## 4. Gestión de Python con `uv`

A diferencia de las instalaciones tradicionales, con `uv` no necesitas instalar Python globalmente en tu sistema. Vamos a descargar la última versión estable (3.12 o superior) para nuestras clases:

```Bash
# Descarga e instala la última versión de Python
uv python install 3.12
```

---

## 5. Inicialización de tu primer proyecto

Vamos a crear la estructura base para el curso siguiendo estándares de **Código Limpio**.

1. **Crea una carpeta para el curso y entra en ella:**

```Bash
mkdir curso-codigo-limpio && cd curso-codigo-limpio
```

2. **Inicializa el proyecto con `uv`:**

```Bash
uv init mi-proyecto-aula
cd mi-proyecto-aula
```

>*Este comando creará automáticamente un archivo `pyproject.toml`, un `README.md` y una carpeta de código fuente.*

3. **Crea el entorno virtual y adición de librerías:** Cuando ejecutes por primera vez tu proyecto, se añadirá de manera automática el directorio `.venv/`, siendo este el entorno virtual que almacena la información de los paquetes usados en el proyecto. Ejecutemos entonces el proyecto:

```Bash
uv run main.py
```

De inmediato te dirá que se creó `.venv/`. Ahora, podremos añadir dependencias. Probemos con añadir `requests`:

```Bash
uv add requests
```

Y listo! Ya tienes tu proyecto funcionando y puedes añadir cuantas dependencias requieras!

---

## 🚀 ¡Listo para programar!

Ahora puedes abrir tu proyecto en **Visual Studio Code** o en el editor de tu preferencia.

*(En caso de usar vscode, asegúrate de aceptar la recomendación de VS Code de instalar la extensión **"WSL"** para que el editor se conecte correctamente con tu terminal de Linux).*
