"""
A validate UID must follow the rules below:

- It must contain at least 2 uppercase English alphabet characters.
- It must contain at least 3 digits (0-9)
- It should only contain alphanumeric characters (a-z,A-Z & 0-9)
- No character should repeat
- There must be exactly 10 characters in valid UID

Input format

The first line contains an integer T, the number of test cases.
The next T lines contains an employee's UID

Output format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.
"""

import pytest
import re

def solution():
    pattern_general = re.compile("[a-zA-Z0-9]{10}")
    pattern_digits = re.compile("[0-9]")
    pattern_uppercase = re.compile("[A-Z]")
    t = int(input())
    for _ in range(t):
        c = input()
        not_duplicate = set(c)
        g = pattern_general.match(c)
        u = pattern_uppercase.findall(c)
        d = pattern_digits.findall(c)
        if len(not_duplicate) == 10 and len(u) >= 2 and len(d) >= 3 and g != None:
            print("Valid")
        else:
            print("Invalid")

monkeypatch = pytest.MonkeyPatch()

def test_one(capsys):
    inputs = iter([
        "2",
        "B1CD102354",
        "B1CDEF2354",
    ])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    
    solution()
    results = """Invalid
Valid
"""
    stdout, stderr = capsys.readouterr()

    assert results == stdout

if __name__ == "__main__":
    solution()