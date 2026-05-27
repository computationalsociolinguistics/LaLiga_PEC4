# La Liga 1996-2025 | Programación Ciencia de Datos (UOC)

**Autor**: Damián Morales Sánchez

## Estructura del proyecto

```
───doc
│       config.html
│       exercises.ex1.html
│       exercises.ex2.html
│       exercises.ex3.html
│       exercises.ex4.html
│       exercises.ex5.html
│       exercises.ex6.html
│       exercises.ex7.html
│       main.html
│       
├───screenshots
│       Captura_ejercicio10.png
│       Captura_ejercicio8.png
│       
├───src
│   │   config.py
│   │   main.py
│   │   __init__.py
│   │   
│   ├───data
│   │       LaLiga_Matches.csv
│   │       
│   ├───exercises
│   │   │   ex1.py
│   │   │   ex2.py
│   │   │   ex3.py
│   │   │   ex4.py
│   │   │   ex5.py
│   │   │   ex6.py
│   │   │   ex7.py
│   │   │   __init__.py
│   │   │   
│   │   
│   │           
│   ├───img
│   │      
│   │       
│   
│           
└───tests
    │   test_ex6.py
    │   
```

## Instalación del proyecto

Se recomienda crear un entorno virtual limpio e instalar las dependencias a partir del archivo `requirements.txt`. Para ello, deben seguirse los siguientes pasos:

1. Crear el entorno virtual en Windows:

```
python -m venv .venv
```

2. Activar el entorno virtual:

```
venv\Scripts\Activate.ps1
```

3. Instalar las dependencias:

```
pip install -r requirements.txt
```

El archivo `requierments.txt` incluye únicamente las librerías necesarias para la correcta ejecución del proyecto:

```
pandas
matplotlib
networkx
```

## Ejecución del proyecto

La ejecución del proyecto se realiza desde el fichero `main.py`. Este archivo ejecuta de forma incrmeental los ejercicios mediante el argumento `-ex número_ejercicio`. Ejemplo:

```
python -u "src/main.py" -ex 3
```

## Comprobación del análisis estático (*linting*)

## Generación de la documentación

La documentación se ha generado automáticamente con la librería *pydoc*. El archivo `docs_generator.py` genera los ficheros `.html` con la documentación de cada módulo del proyecto. Estos archivos están ubicados en la carpeta `doc/` del proyecto.

Documentación generada:

```
main.html
config.html
exercises.ex1.html
exercises.ex2.html
exercises.ex3.html
exercises.ex4.html
exercises.ex5.html
exercises.ex6.html
exercises.ex7.html
```

## Comprobación de los tests

El proyecto incluye un test unitario para verificar el funcionamiento de la función `fun_total_goals()`, definida en el fichero `src/exercises/ex6.py`.

El test se incluye en el fichero `tests/test_ex6.py`.

La ejecución del test se realiza mediante el siguiente código:

```
python -m unittest tests.test_ex6
```
## Subir el proyecto a Github

```
git init
git config --global user.name "computationalsociolinguistics"
git config --global user.email "computationalsociolinguistics@gmail.com"
git add doc/ src/ tests/
git commit -m 'Commit inicial proyecto'
git branch -M main
git remote add origin https://github.com/USUARIO/LaLiga_PEC4.git
git push -u origin main
```

## Licencia

Este proyecto se distribuye bajo la liencia **MIT**.