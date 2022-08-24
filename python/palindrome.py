import unittest
class Palindrome(object):
    def __init__(self, n, l):
        self.n = n
        self.l = l
    
    def palindrome(self):
        check = []
        result = []
        for i in range(self.n):
            if self.l[i] >= 0:
                check.append(True)
            else:
                check.append(False)

        if all(check):
            result.append(True)
        else:
            result.append(False)
            
        check.clear()

        for x in self.l:
            x_str = str(x)
            if len(x_str) == 1:
                check.append(True)
            else:
                if x_str == x_str[::-1]:
                    check.append(True)
                else:
                    check.append(False)

        if any(check):
            result.append(True)
        else:
            result.append(False)

        return all(result)

class TestPalindrome(unittest.TestCase):
    def __init__(self,methodName: str = ...) -> None:
        super().__init__(methodName)
        n = 6
        l = [1, 2, 3, 4, 5, -9]
        self.pali = Palindrome(n,l)
    
    def test_palindrome(self):
        self.assertEqual(False, self.pali.palindrome())

if __name__ == '__main__':
    unittest.main()