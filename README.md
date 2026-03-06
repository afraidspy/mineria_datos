<table border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td width="38%" valign="middle" style="padding-right: 18px;">
      <img src="imgs/fciencias.webp" alt="UNAM y Facultad de Ciencias" width="360" />
    </td>
    <td valign="middle">
      <p style="margin: 0; font-size: 28px; font-weight: 700;">
        Universidad Nacional Autónoma de México
      </p>
      <p style="margin: 6px 0 0 0; font-size: 20px; font-weight: 600;">
        Facultad de Ciencias
      </p>
      <p style="margin: 12px 0 0 0; font-size: 18px; font-weight: 600;">
        Almacenes y Minería de Datos
      </p>
      <p style="margin: 6px 0 0 0; font-size: 16px;">
        Profesora: MSc Data Analytics Jessica Santizo Galicia
      </p>
    </td>
  </tr>
</table>

---

# Introducción

Este repositorio contiene materiales de apoyo para la asignatura **Almacenes y Minería de Datos**, incluyendo notebooks, prácticas, datasets de ejemplo y guías de instalación.

En la parte de **almacenes de datos**, trabajaremos conceptos como:
- Modelado dimensional (hechos y dimensiones)
- Procesos ETL/ELT (extracción, transformación y carga)
- Calidad de datos y documentación
- Consultas y análisis para apoyar la toma de decisiones

En la parte de **minería de datos**, practicaremos tareas como:
- Análisis exploratorio y preparación de datos
- Clasificación y regresión
- Agrupamiento (clustering)
- Detección de anomalías
- Reglas de asociación

---

# Instalación y ejecución (entorno virtual)

## Requisitos previos
1. **Python 3.11 o superior** instalado.
2. **pip** disponible (normalmente viene con Python).
3. Una terminal (por ejemplo, la terminal integrada de VS Code, PowerShell/CMD en Windows, o Terminal en macOS/Linux).

Verifica que Python y pip funcionan:

```bash
python --version
pip --version
```

En macOS/Linux, si `python` no funciona, prueba:

```bash
python3 --version
pip3 --version
```

---

## Crear y activar el entorno virtual

Asegúrate de estar en la carpeta del proyecto (donde está `requirements.txt`).

### Windows

1) Crear el entorno virtual

```bash
python -m venv .venv
```

Si `python` no existe pero `py` sí:

```bash
py -m venv .venv
```

2) Activar el entorno

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

CMD:

```bat
.\.venv\Scripts\activate.bat
```

3) Instalar dependencias

```bash
pip install -r requirements.txt
```

4) Verificar que estás usando el entorno

```bash
python -c "import sys; print(sys.executable)"
pip --version
```

---

### macOS / Linux / Unix

1) Crear el entorno virtual

```bash
python3 -m venv .venv
```

2) Activar el entorno

```bash
source .venv/bin/activate
```

3) Instalar dependencias

```bash
pip install -r requirements.txt
```

4) Verificar que estás usando el entorno

```bash
python -c "import sys; print(sys.executable)"
pip --version
```

---

## Uso diario

- Activa el entorno cada vez que vayas a trabajar en el proyecto.
- Para salir del entorno:

```bash
deactivate
```

---

## Problemas comunes

### Actualizar pip
Dentro del entorno virtual:

```bash
python -m pip install --upgrade pip
```

### VS Code no detecta el entorno
- Abre la paleta de comandos: `Ctrl + Shift + P`
- Busca: **Python: Select Interpreter**
- Elige el intérprete dentro de `.venv`

---

© 2026 Jessica Santizo Galicia. Todos los derechos reservados.
# mineria_datos
