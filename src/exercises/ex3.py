'''
Ejercicio 3 PEC 4
Autor: Damián Morales Sánchez
'''
import pandas as pd
import matplotlib.pyplot as plt
from src import config

def goals_distribution(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    '''
    Genera dos dataframes (distr_goals_home y distr_goals_away) con el número de
    goles anotados como índice y el número de partidos en que se han marcado.

    Arguments:
      data (pandas.DataFrame): El conjunto de datos.

    Returns:
      tuple[pandas.DataFrame, pandas.DataFrame]: Los dataframes distr_goals_home
      y distr_goals_away con la distribución de goles marcados y el número de partidos
      de los equipos locales y visitantes.
    '''
    distr_goals_home = pd.DataFrame({'Matches': data['FTHG'].value_counts().sort_index()})

    distr_goals_away = pd.DataFrame({'Matches': data['FTAG'].value_counts().sort_index()})

    return distr_goals_home, distr_goals_away

def plot_goals_distribution(distr_goals_home: pd.DataFrame, distr_goals_away: pd.DataFrame) -> None:
    '''
    Genera dos gráficos de barras con la distribución de goles marcados y el número
    de partidos en que se han marcado por los equipos locales y visitantes.

    Arguments:
      distr_goals_home (pandas.DataFrame): El dataframe con la distribución de goles
      y partidos de los equipos locales.
      distr_goals_away (pandas.DataFrame): El dataframe con la distribución de goles
      y partidos de los equipos visitantes.

    Returns:
      None
    '''

    plt.figure(figsize=(10, 10))

    plt.subplot(2, 1, 1)
    plt.bar(distr_goals_home.index,
          distr_goals_home['Matches'])

    plt.title('Distribución de goles marcados por los equipos locales')
    plt.xlabel('Número de goles')
    plt.ylabel('Número de partidos')

    plt.subplot(2, 1, 2)
    plt.bar(distr_goals_away.index, distr_goals_away['Matches'])

    plt.title('Distribución de goles marcados por los equipos visitantes')
    plt.xlabel('Número de goles')
    plt.ylabel('Número de partidos')

    plt.tight_layout()
    plt.savefig(f'src/img/grafica_ex3_{config.NOM_ALUMNE}_{config.date_time}.png')
    plt.show()
