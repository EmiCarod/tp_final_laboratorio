 # TP Final de Laboratorio

Descripción del proyecto: aplicación desarrollada para el trabajo final de laboratorio. Este repositorio contiene el código fuente y las pruebas automatizadas del proyecto.

## Instalación

Se requiere Python 3 y `pip`. Desde la carpeta del proyecto, crea y activa un entorno virtual:


python -m venv .venv
venv\Scripts\activate

Instala las dependencias:

```bash
python -m pip install 
pip install -r requirements.txt
```

## Ejecución de la aplicación

Con el entorno virtual activo, ejecuta el punto de entrada del proyecto. Por ejemplo:

```bash
python main.py
```


## Pruebas

Ejecuta la suite de pruebas con pytest:

```bash
pytest