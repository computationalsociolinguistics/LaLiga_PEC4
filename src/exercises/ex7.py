'''
Ejercicio 7 PEC 4
Autor: Damián Morales Sánchez
'''
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from src import config

def graf(data: pd.DataFrame, selected_teams: list[str]) -> None:
    '''
    Genera un grafo de conexiones entre los equipos con mejor puntuación acumulada.

    Arguments:
      data (pandas.DataFrame): El conjunto de datos con la información de los equipos.
      selected_teams (list[str]): La lista con los cinco equipos que han obtenido
      la mejor puntuación acumulada.

    Returns:
      None
    '''

    data_filtrada = data[(data['HomeTeam'].isin(selected_teams)) &
                         (data['AwayTeam'].isin(selected_teams))]

    graph = nx.Graph()

    graph.add_nodes_from(selected_teams)

    conexiones = (data_filtrada.apply(
      lambda fila: tuple(sorted([fila['HomeTeam'], fila['AwayTeam']])), axis=1).value_counts())

    for (equipo_a, equipo_b), weight in conexiones.items():
        graph.add_edge(equipo_a, equipo_b, weight=weight)

    pos = nx.spring_layout(graph, seed=42)

    plt.figure(figsize=(10, 10))

    nx.draw_networkx_nodes(graph, pos, node_size=2500)

    nx.draw_networkx_labels(graph, pos, font_size=8)

    nx.draw_networkx_edges(graph, pos, width=1.5, edge_color='red')

    nx.draw_networkx_edge_labels(graph, pos,
    edge_labels=nx.get_edge_attributes(graph, 'weight'),
    font_size=8)

    plt.title('Grafo de partidos disputados entre los 5 mejores equipos')
    plt.tight_layout()
    plt.savefig(f'src/img/grafica_ex7_{config.NOM_ALUMNE}_{config.date_time}.png')
    plt.show()
