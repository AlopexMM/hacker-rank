from unittest import TestCase
from unittest.mock import patch
import collections_deque_h

class TestCollectionsDeque(TestCase):

    def test_collections_deque_main(self):
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:

                inputs = (
                    '6',
                    'append 1',
                    'append 2',
                    'append 3',
                    'appendleft 4',
                    'pop',
                    'popleft' 
                )

                mocked_input.side_effect = inputs

                collections_deque_h.main()

                mocked_print('1 2')