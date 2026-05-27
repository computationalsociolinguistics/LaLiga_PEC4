import pandas as pd
import matplotlib.pyplot as plt
from src import config

def total_matches(data: pd.DataFrame) -> pd.DataFrame:
  '''
  Devuelve un dataframe con el número total de partidos jugados (en orden descendente)
  por cada equipo durante todos los años registrados.

  Arguments:
    data (pandas.DataFrame): El conjunto de datos.

  Returns:
    pandas.DataFrame: El dataframe matches_team_total con el total de
    partidos jugados por cada equipo.
  '''

  home_matches = data['HomeTeam'].value_counts()
  away_matches = data['AwayTeam'].value_counts()
  matches_team_total = pd.DataFrame({'Total matches': home_matches+away_matches}).sort_values(by='Total matches', ascending=False)

  return matches_team_total

def plot_matches_team_total(matches_team_total: pd.DataFrame) -> None:
  '''
  Genera un gráfico de barras con el número total de partidos disputados por cada
  equipo.

  Arguments:
    matches_team_total (pandas.DataFrame): El conjunto de datos con el número
    total de partidos jugados por cada equipo.

  Returns:
    None
  '''

  plt.figure(figsize=(10, 10))

  plt.bar(matches_team_total.index,
          matches_team_total['Total matches'])

  plt.plot(matches_team_total.index,
           matches_team_total['Total matches'],
           marker='_',
           color='black')

  plt.title('Partidos disputados por los equipos de fútbol')
  plt.xlabel('Equipos')
  plt.ylabel('Número total de partidos')

  plt.xticks(rotation=90)
  plt.tight_layout()
  plt.savefig(f'src/img/grafica_ex2_{config.nom_alumne}_{config.date_time}.png')
  plt.show()

  return None