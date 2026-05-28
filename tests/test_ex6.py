import unittest
import pandas as pd

from src.exercises.ex6 import fun_total_goals

class TestFunTotalGoals(unittest.TestCase):
    '''
    Suite de tests para la función fun_total_goals.
    '''

    def test_goals(self):
        '''
        Comprueba que la función realice correctamente el cómputo
        de goles.
        '''

        test_dataframe = pd.DataFrame({
            'FTHG': [1, 0, 5, 4, 3],
            'FTAG': [2, 2, 1, 0, 4]
        })

        home_goals, away_goals, total_goals = fun_total_goals(test_dataframe)

        self.assertTrue(home_goals == 13)
        self.assertTrue(away_goals == 9)
        self.assertTrue(total_goals == 22)
    
    def test_empty(self):
        '''
        Comprueba que los dataframes están vacíos.
        '''

        test_dataframe_2 = pd.DataFrame({
            'FTHG': [],
            'FTAG': []
        })

        home_goals, away_goals, total_goals = fun_total_goals(test_dataframe_2)

        self.assertFalse(home_goals)
        self.assertFalse(away_goals)
        self.assertFalse(total_goals)
    
    def test_one_match(self):
        '''
        Verifica el cómputo con un solo partido.
        '''
        test_dataframe_3 = pd.DataFrame({
            'FTHG': [4],
            'FTAG': [1]
        })
    
        home_goals, away_goals, total_goals = fun_total_goals(test_dataframe_3)

        self.assertTrue(home_goals == 4)
        self.assertFalse(away_goals == 2)
        self.assertTrue(total_goals == 5)

    if __name__ == '__main__':
        unittest.main()

