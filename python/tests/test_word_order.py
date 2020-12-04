from unittest import TestCase
from unittest.mock import patch
import word_order

class TestWordOrder(TestCase):
    def test_word_order_main(self):
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                inputs = (
                    '4',
                    'bcdef',
                    'abcdefg',
                    'bcde',
                    'bcdef'
                )

                mocked_input.side_effect = inputs

                word_order.main()

                mocked_print.assert_called_with('3\n2 1 1 ')
