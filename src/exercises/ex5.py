'''
Ejercicio 5 PEC 4
Autor: Damián Morales Sánchez
'''
import pandas as pd

def add_points(data: pd.DataFrame) -> pd.DataFrame:
    '''
    Añade al dataset los puntos conseguidos en cada partido por los equipos locales
    y visitantes. Devuelve el conjunto de datos con las columnas points_home
    y points_away.

    Arguments:
      data (pandas.DataFrame): El conjunto de datos con la información de los partidos.
  
    Returns:
      pandas.DataFrame: El dataframe con las columnas points_home y points_away.
    '''

    data['points_home'] = data['FTR'].map({'H': 3, 'A': 0, 'D': 1})
    data['points_away'] = data['FTR'].map({'H': 0, 'A': 3, 'D': 1})

    return data

def fun_total_points(data: pd.DataFrame) -> tuple[pd.Series, pd.DataFrame]:
    '''
    Calcula el total de puntos obtenidos y acumulados desde 1995 por cada equipo.

    Arguments:
      data (pandas.DataFrame): El conjunto de datos con la información de los partidos.
  
    Returns:
      tuple[pandas.Series, pandas.DataFrame]: Una tupla con la serie y el dataframe
      con los puntos totales acumulados por los equipos.  
    '''

    home_points = data.groupby('HomeTeam')['points_home'].sum()
    away_points = data.groupby('AwayTeam')['points_away'].sum()
    total_points = home_points.add(away_points).sort_values(ascending=False)
    df_total_points = total_points.to_frame(name='Total points')

    return total_points, df_total_points

def alltime_winner(df_total_points: pd.DataFrame) -> str:
    '''
    Devuelve el equipo ganador de la liga histórica (el equipo con más puntos).

    Arguments:
      df_total_points (pandas.DataFrame): El dataframe con los puntos acumulados
      por los equipos.
  
    Returns:
      str: Nombre del equipo ganador con más puntos acumulados.
    '''
    ganador = df_total_points.index[0]

    return ganador
