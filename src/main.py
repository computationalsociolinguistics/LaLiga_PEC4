from exercises.ex1 import load_and_eda, plot_home_away
from exercises.ex2 import total_matches, plot_matches_team_total
from exercises.ex3 import goals_distribution, plot_goals_distribution
from exercises.ex4 import FTR, plot_FTR
from exercises.ex5 import add_points, fun_total_points, alltime_winner
from exercises.ex6 import fun_total_goals, fun_total_goals_by_team, fun_summary_1996_2025, podium
from exercises.ex7 import graf


import argparse


def main() -> None:
    '''
    Ejecuta los ejercicios de la PEC4 de manera incremental.

    Arguments:
      None
    
    Returns:
      None
    '''
    parser = argparse.ArgumentParser(
        description='Proyecto Damián Morales Sánchez PEC4'
    )

    parser.add_argument(
        '-ex',
        type=int,
        choices=range(1, 8),
        help='Ejecuta los ejercicios de forma incremental'
    )

    args = parser.parse_args()

    if args.ex >= 1:
        print('-----EJERCICIO 1-----\n')

        file = 'src/data/LaLiga_Matches.csv'
        
        data = load_and_eda(file)

        plot_home_away(data)
    
    if args.ex >=2:
        print('-----EJERCICIO 2-----\n')

        total_matches(data)

        matches_team_total = total_matches(data)

        print(matches_team_total.head(10), '\n')

        print('Los equipos que han estado siempre en primera división son:\n')
        print(matches_team_total[matches_team_total['Total matches'] == matches_team_total['Total matches'].max()])

        plot_matches_team_total(matches_team_total)

    if args.ex >=3:
        print('-----EJERCICIO 3-----\n')

        print(goals_distribution(data))

        distr_goals_home, distr_goals_away = goals_distribution(data)

        plot_goals_distribution(distr_goals_home, distr_goals_away)

    if args.ex >=4:
        print('-----EJERCICIO 4-----\n')

        FTR(data)

        ftr = FTR(data)

        print(ftr.head(), '\n')

        home_win = ftr.loc['H', 'Number of matches'] / ftr['Number of matches'].sum() * 100
        print(f'El porcentaje de victorias locales se sitúa en un {home_win:.2f}%.')

        plot_FTR(ftr)
    
    if args.ex >=5:
        print('-----EJERCICIO 5-----\n')

        data = add_points(data)

        print(data.head(10), '\n')

        fun_total_points(data)

        total_points, df_total_points = fun_total_points(data)

        print(df_total_points.head(10), '\n')

        alltime_winner(df_total_points)

        print(f'El equipo ganador de la liga histórica es {alltime_winner(df_total_points).upper()}.')

    if args.ex >=6:
        print('-----EJERCICIO 6-----\n')

        fun_total_goals(data)

        home_goals, away_goals, total_goals = fun_total_goals(data)
        print(f'Los equipos locales han anotado un total de {home_goals} goles.')
        print(f'Los equipos visitantes han anotado un total de {away_goals} goles.')
        print(f'En total se han anotado {total_goals} goles.')
        
        fun_total_goals_by_team(data)

        home_goals_by_team, away_goals_by_team, total_goals_by_team = fun_total_goals_by_team(data)
        print(total_goals_by_team.head(10), '\n')

        total_points_by_team = df_total_points

        summary_1996_2025 = fun_summary_1996_2025(total_points_by_team, home_goals_by_team, away_goals_by_team, total_goals_by_team)
        print(summary_1996_2025.head(), '\n')

        podium(summary_1996_2025)

    if args.ex >=7:
        print('-----EJERCICIO 7-----\n')
        
        selected_teams = df_total_points.head().index.tolist()

        graf(data, selected_teams)

if __name__ == "__main__":
    main()