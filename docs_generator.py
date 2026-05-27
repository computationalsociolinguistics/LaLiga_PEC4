import os

modules = [
    "main",
    "config",
    "exercises.ex1",
    "exercises.ex2",
    "exercises.ex3",
    "exercises.ex4",
    "exercises.ex5",
    "exercises.ex6",
    "exercises.ex7",
]


for module in modules:
    os.system(f"cd src && python -m pydoc -w {module}")
