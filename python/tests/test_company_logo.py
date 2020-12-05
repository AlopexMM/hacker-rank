from unittest import TestCase
from unittest.mock import patch
import company_logo

class TestCompanyLogo(TestCase):
    def test_comany_logo_main(self):
        with patch('builtins.input', return_value="aabbbccde") as mocked_input:
            with patch('builtins.print') as mocked_print:

                company_logo.main()

                mocked_print.assert_called_with('b 3\na 2\nc 2\n')
    
    def test_comany_logo_main_2(self):
        with patch('builtins.input', return_value="qwertyuiopasdfghjklzxcvbnm") as mocked_input:
            with patch('builtins.print') as mocked_print:

                company_logo.main()

                mocked_print.assert_called_with('a 1\nb 1\nc 1\n')