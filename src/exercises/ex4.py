'''
Ejercicio 4 PEC 4
Autor: Damián Morales Sánchez
'''
import pandas as pd
import matplotlib.pyplot as plt
from src import config

def FTR(data: pd.DataFrame) -> pd.DataFrame:
    '''
    Devuelve un dataframe con el número de partidos ganados por los equipos locales
    y visitantes, así como los encuentros empatados.

    Arguments:
      data (pandas.DataFrame): El conjunto de datos.

    Returns:
      pandas.DataFrame: El dataframe ftr con el número de partidos ganados por los
      equipos locales y visitantes, y partidos empatados.
    '''

    ftr = pd.DataFrame({'Number of matches': data['FTR'].value_counts()})

    return ftr

def plot_FTR(ftr: pd.DataFrame) -> None:
    '''
    Genera un gráfico de barras con el número de partidos ganados por los equipos
    locales y visitantes, y partidos empatados.

    Arguments:
      ftr (pandas.DataFrames): El conjunto de datos con el número de partidos
      según el resultado (H, A y D).
  
    Returns:
      None
    '''

    plt.figure(figsize=(7, 5))

    plt.bar(ftr.index, ftr['Number of matches'],
          color=['lightgreen', 'lightblue', 'lightcoral'])
    plt.title('Distribución del número de partidos según el resultado final')
    plt.xlabel('Resultado final')
    plt.ylabel('Número de partidos')

    colors = {'H - Victoria local': 'lightgreen',
            'A - Victoria visitante': 'lightblue',
            'D - Empate': 'lightcoral'}
    labels = list(colors.keys())
    handles = [plt.Rectangle((0, 0), 1, 1, color=colors[label]) for label in labels]
    plt.legend(handles, labels)

    plt.tight_layout()
    plt.savefig(f'src/img/grafica_ex4_{config.NOM_ALUMNE}_{config.date_time}.png')
    plt.show()
