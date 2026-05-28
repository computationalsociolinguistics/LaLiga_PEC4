# La Liga 1996-2025 | Programación Ciencia de Datos (UOC)

**Autor**: Damián Morales Sánchez

## Definición del proyecto

Este proyecto se enmarca en la PEC4 de la asignatura *Programación para la ciencia de datos* de la Universitat Oberta de Catalunya (UOC). El objetivo principal es el desarrollo de un proyecto Python fuera del entorno de los cuadernos interactivos (*.ipynb*). Para ello, se resuelven siete ejercicios vinculados con el análisis de un conjunto de datos de la liga española de fútbol que contiene información sobre los partidos disputados desde 1995 hasta 2025. Además, se incluyen los archivos de documentación de alto nivel y los archivos de licencia y dependencias.

## Estructura del proyecto

```
proyecto/
├── doc/                      # Documentacióm generada con pydoc
│     ├── config.html
│     ├── exercises.ex1.html
│     ├── exercises.ex2.html
│     ├── exercises.ex3.html
│     ├── exercises.ex4.html
│     ├── exercises.ex5.html
│     ├── exercises.ex6.html
│     ├── exercises.ex7.html
│     └── main.html
│       
├── screenshots/              # Capturas de pantalla
│             
├── src/
│   ├── config.py             # Documento con las variables globales
│   ├── main.py               # Documento principal para la ejecución del proyecto
│   ├── __init__.py
│   │   
│   ├── data/                 # Conjunto de datos analizado
│   │    └── LaLiga_Matches.csv
│   │       
│   ├── exercises/            # Funciones de los ejercicios 1 a 7
│   │   ├── ex1.py
│   │   ├── ex2.py
│   │   ├── ex3.py
│   │   ├── ex4.py
│   │   ├── ex5.py
│   │   ├── ex6.py
│   │   ├── ex7.py
│   │   └── __init__.py
│   │   
│   └── img/                 # Gráficos de los ejercicios                              
├── tests                    # Tests unitarios
│   └── test_ex6.py    
├── .pylintrc                # Configuración de pylint               
├── generate_docs.py         # Script para generar automáticamente la documentación
├── LICENSE                  # Licencia del proyecto
├── README.md                # Información general del proyecto
└── requirements.txt         # Dependencias necesarias 
```

## Instalación del proyecto

Se recomienda instalar el proyecto y las dependencias (a partir del archivo `requirements.txt`). en un entorno virtual limpio. Para ello, deben seguirse los siguientes pasos:

### 1. Clonar el proyecto

```
git clone https://github.com/computationalsociolinguistics/LaLiga_PEC4.git
```

### 2. Crear el entorno virtual

#### Windows:

```
python -m venv .venv
```
#### Linux /macOs

```
python3 -m venv .venv
```

### 3. Activar el entorno virtual:

#### Windows (Powershell)
```
venv\Scripts\Activate.ps1
```

#### Windows (CMD)

```
venv\Scripts\activate
```

#### Linux / macOs

```
source venv/bin/activate
```

Tras la activación, el terminal mostrará el nombre del entorno:

```
(venv)
```
### 4. Instalar las dependencias:

Con el entorno activado, instalar las librerías:

```
pip install -r requirements.txt
```

El archivo `requirements.txt` incluye únicamente las librerías necesarias para la correcta ejecución del proyecto:

```
pandas
matplotlib
networkx
```

## Ejecución del proyecto

La ejecución del proyecto se realiza desde el fichero `main.py`. Este archivo ejecuta de forma incremental los ejercicios mediante el argumento `-ex X`. El siguiente ejemplo ejecutaría las funciones de los ejercicios 1, 2 y 3:

```
python -m src.main -ex 3
```


## Comprobación del análisis estático (*linting*)

Este proyecto sigue la guía de estilo PEP8. Emplea la librería `pylint` para analizar la calidad del código y subsanar posibles errores. 

### Instalación de pylint

```
pip install pylint
```

Para realizar el análisis estático debe ejecutarse desde la raíz del proyecto:

```
pylint src
```

También se pueden analizar módulos concretos:

```
pylint src/exercises/ex1.py
```
## Generación de la documentación

La documentación se ha generado automáticamente con la librería [*pydoc*](https://docs.python.org/es/3.9/library/pydoc.html). El archivo `docs_generator.py` genera los ficheros `.html` con la documentación de cada módulo del proyecto. Estos archivos están ubicados en la carpeta `doc/` del proyecto.

Documentación generada:

```
config.html
exercises.ex1.html
exercises.ex2.html
exercises.ex3.html
exercises.ex4.html
exercises.ex5.html
exercises.ex6.html
exercises.ex7.html
main.html
```

## Comprobación de los tests

El proyecto incluye un test unitario para verificar el funcionamiento de la función `fun_total_goals()`, definida en el fichero `src/exercises/ex6.py`.

El test se incluye en el fichero `tests/test_ex6.py`.

La ejecución del test se realiza mediante el siguiente código:

```
python -m unittest tests.test_ex6
```
## Subir el proyecto a Github

Con el propósito de subir el proyecto a un repositorio remoto de GitHub y llevar a cabo un control de versiones, se siguieron los siguientes pasos:

### 1. Inicializar el repositorio Git

```
git init
```

### 2. Configurar el usuario de Git

```
git config --global user.name "computationalsociolinguistics"
git config --global user.email "computationalsociolinguistics@gmail.com"
```

### 3. Añadir los archivos 
```
git add doc/ src/ tests/
```

### 4. Crear el primer commit

```
git commit -m 'Commit inicial proyecto'
```

### 5. Renombrar la rama principal 

```
git branch -M main
```

### 6. Vincular el repositorio local con GitHub

```
git remote add origin https://github.com/USUARIO/LaLiga_PEC4.git
```

### 7. Subir el proyecto a GitHub

```
git push -u origin main
```

Tras la configuración inicial, los cambios se introducen con el siguiente flujo de código:

```
git add
git commit -m 'Explicación de los cambios'
git push
```

## Licencia

Este proyecto se distribuye bajo la liencia **MIT**.