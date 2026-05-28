'''
Ejercicio 6 PEC 4
Autor: Damián Morales Sánchez
'''
import pandas as pd
import matplotlib.pyplot as plt
from src import config

def fun_total_goals(data: pd.DataFrame) -> tuple[int, int, int]:
    '''
    Calcula el número total de goles marcados por los equipos locales, visitantes
    y el total general.

    Arguments:
      data (pandas.DataFrame): El dataframe con la información de los partidos.

    Returns:
      tuple[int, int, int]: Una tupla con el número total de goles locales, visitantes
      y goles totales.
    '''

    home_goals = int(data['FTHG'].sum())
    away_goals = int(data['FTAG'].sum())
    total_goals = home_goals + away_goals

    return home_goals, away_goals, total_goals

def fun_total_goals_by_team(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    '''
    Genera tres dataframes (home_goals_by_team, away_goals_by_team,
    total_goals_by_team) con el número total de goles marcados por los equipos locales,
    visitantes y el total general.

    Arguments:
      data (pandas.DataFrame): El conjunto de datos con la información sobre los partidos.
  
    Returns:
      tuple[pandas.DataFrame, pandas.DataFrame, pandas.DataFrame]: Una tupla
      con los tres dataframes con los goles anotados por los equipos locales, visitantes
      y goles totales por equipos.
    '''

    home_goals_by_team = data.groupby('HomeTeam')['FTHG'].sum().to_frame(name='Home goals')
    away_goals_by_team = data.groupby('AwayTeam')['FTAG'].sum().to_frame(name='Away goals')
    total_goals_by_team = home_goals_by_team['Home goals'].add(away_goals_by_team['Away goals'])
    total_goals_by_team = total_goals_by_team.to_frame(name='Total goals').sort_values(
        by='Total goals', ascending=False)

    return home_goals_by_team, away_goals_by_team, total_goals_by_team

def fun_summary_1996_2025(
    total_points_by_team: pd.DataFrame,
    home_goals_by_team: pd.DataFrame,
    away_goals_by_team: pd.DataFrame,
    total_goals_by_team: pd.DataFrame
) -> pd.DataFrame:

    '''
    Crea un dataframe (summary_1996_2025) con un resumen de los puntos totales,
    goles locales, goles visitantes y goles totales por cada equipo.

    Arguments:
      total_points_by_team (pandas.DataFrame): El dataframe con los puntos totales
      por equipo.
      home_goals_by_team (pandas.DataFrame): El dataframe con los goles locales por
      equipo.
      away_goals_by_team (pandas.DataFrame): El dataframe con los goles visitantes por
      equipo.
      total_goals_by_team (pandas.DataFrame): El dataframe con los goles totales por
      equipo.

    Returns:
      pandas.DataFrame: El dataframe summary_1996_2025 con los puntos totales, 
      goles anotados como local, goles anotados como visitante y goles totales por
      equipo.
    '''

    summary_1996_2025 = pd.concat(
        [
            total_points_by_team,
            home_goals_by_team,
            away_goals_by_team,
            total_goals_by_team
      ],axis=1
    )

    return summary_1996_2025

def podium(summary_1996_2025: pd.DataFrame) -> None:
    '''
    Genera un grafico de barras con los tres mejores equipos históricos a
    modo de podium.

    Arguments:
      summary_1996_2025 (pandas.DataFrame): El dataframe con los puntos totales,
      goles anotados como local, goles anotados como visitante y goles totales por
      equipo.

    Returns:
      None
    '''

    podio_equipos = summary_1996_2025.head(3)

    equipos = [podio_equipos.index[1], podio_equipos.index[0], podio_equipos.index[2]]

    y = [2, 3, 1]

    plt.figure(figsize=(7, 5))

    plt.bar(equipos,
          y,
          color=['whitesmoke', '#004D98', '#CB3524'],
          edgecolor='black')

    for i, equipo in enumerate(equipos):
        plt.text(i,
                 y[i]+0.05,
                 equipo,
                 ha='center',
                 fontsize=8)


    plt.title('Podium histórico La Liga 1996-2025')
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()
    plt.savefig(f'src/img/grafica_ex6_{config.NOM_ALUMNE}_{config.date_time}.png')
    plt.show()
