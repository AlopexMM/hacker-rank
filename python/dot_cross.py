import numpy

def main():
    n = int(input())

    a = []
    b = []

    for _ in range(n):
        a.append(list(map(int,input().split(" "))))

    for _ in range(n):
        b.append(list(map(int,input().split(" "))))
    
    print(numpy.dot(a,b))

if __name__ == "__main__":
    main()

import pytest

monkeypatch = pytest.MonkeyPatch()

def test_cero(capsys):
    inputs = iter([
        "2",
        "1 2",
        "3 4",
        "1 2",
        "3 4",
    ])

    results = """[[ 7 10]
 [15 22]]\n"""
    
    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    main()

    stdout, stderr = capsys.readouterr()

    assert results == stdout