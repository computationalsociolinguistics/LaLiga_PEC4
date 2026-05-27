import unittest
import pandas as pd

from src.exercises.ex6 import fun_total_goals

class TestFunTotalGoals(unittest.TestCase):

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

    if __name__ == '__main__':
        unittest.main()
