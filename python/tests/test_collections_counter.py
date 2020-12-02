from unittest import TestCase
from unittest.mock import patch
import collections_counter_h

class TestCollectionsCounte(TestCase):

    def test_colections_counter_main_case_1(self):
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                inputs = (
                    '10', # Total shoes he has
                    '2 3 4 5 6 8 7 6 5 18', # shoes in the store per size
                    '6', # how many customers has that day
                    '6 55', # size shoes, money pay if that shoe is in the store 
                    '6 45',
                    '6 55',
                    '4 40',
                    '18 60',
                    '10 50'
                )

                mocked_input.side_effect = inputs
                
                collections_counter_h.main()
                
                mocked_print.assert_called_with(200)