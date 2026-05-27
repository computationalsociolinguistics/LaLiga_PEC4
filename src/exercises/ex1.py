import pandas as pd
import matplotlib.pyplot as plt
from src import config

def load_and_eda(file: str) -> pd.DataFrame:
  '''
  Carga el dataset y elimina las columnas "HTHG", "HTAG" y "HTR".
  Muestra las primeras y últimas filas del conjunto de datos y la información
  más relevante.

  Arguments:
    file (str): Camino relativo del dataset.

  Returns:
    pandas.DataFrame: El conjunto de datos sin las columnas "HTGH", "HTAG" y "HTR".
  '''
  df = pd.read_csv(file)

  df = df.drop(columns=['HTHG', 'HTAG', 'HTR'])

  print('Primeras filas del dataset:\n')
  print(df.head(), '\n')
  print('Últimas filas del dataset:\n')
  print(df.tail(), '\n')
  print('Información relevante del dataset:\n')
  df.info()
  print()
  print(df.describe(), '\n')

  return df

def plot_home_away(data: pd.DataFrame) -> None:
  '''
  Genera una figura con dos boxplot con la distribución de goles marcados por
  los equipos locales y por los equipos visitantes.

  Arguments:
    data (pandas.DataFrame): El conjunto de datos.

  Returns:
    None
  '''

  plt.figure(figsize=(11, 11))

  plt.subplot(2, 1, 1)
  plt.boxplot(data['FTHG'],
              showmeans=True)
  plt.title('Distribución de goles marcados por los equipos locales')
  plt.xlabel('Equipos locales (HomeTeam)')
  plt.ylabel('Goles marcados')

  plt.subplot(2, 1, 2)
  plt.boxplot(data['FTAG'],
              showmeans=True)
  plt.title('Distribución de goles marcados por los equipos visitantes')
  plt.xlabel('Equipos visitantes (AwayTeam)')
  plt.ylabel('Goles marcados')

  plt.tight_layout()
  plt.savefig(f'src/img/grafica_ex1_{config.nom_alumne}_{config.date_time}.png')
  plt.show()

  return None