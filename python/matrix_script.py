"""
Neo has a complex matrix script. 
The matrix script is a N x M grid of strings. 
It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. 
Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.

Neo feels that there is no need to use 'if' conditions for decoding.

Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

Input Format

The first line contains space-separated integers N (rows) and M (columns) respectively.
The next N lines contain the row elements of the matrix script.

Cantraints

0 < N, M < 100

Sample Input 0

7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!

Sample Output 0

This is Matrix#  %!
"""
import pytest
import re

def solution():
    n, m = list(map(int,input().split()))

    matrix = []

    for _ in range(n):
        matrix_item = [x for x in input()]
        matrix.append(matrix_item)
    phrase = ""
    for x in range(m):
        for y in range(n):
            phrase += matrix[y][x]
    # Alphanumeric character follow by symbols !,@,#,$,%,& but not black space or symbol follow by space follow by alphanumeric
    regex = r"(?<=\w)([^\w]+)(?=\w)"
    subst = " "
    result = re.sub(regex,subst,phrase,0,re.MULTILINE) 
    print(result)

monkepatch = pytest.MonkeyPatch()

def test_cero(capsys):
    inputs = iter([
        "7 3",
        "Tsi",
        "h%x",
        "i #",
        "sM ",
        "$a ",
        "#t%",
        "ir!",
    ])

    monkepatch.setattr("builtins.input", lambda: next(inputs))

    results = "This is Matrix#  %!\n"
    solution()
    stdout, stderr = capsys.readouterr()

    

    assert stdout == results

def test_one(capsys):
    inputs = iter([
        "5 9",
        "#%$r%r$n ",
        "O%Mi$iTi$",
        "yiaxsprt ",
        "est%ctiy#",
        "  t c i %",
    ])

    monkepatch.setattr("builtins.input", lambda: next(inputs))

    results = "#Oye is Mattrix sccript Triinity  $ #%\n"
    solution()
    stdout, stderr = capsys.readouterr()

    

    assert stdout == results


if __name__ == '__main__':
    solution()
