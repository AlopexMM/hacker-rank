import numpy

def main():
    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(float,input().split(" "))))
    
    array = numpy.array(arr)

    determinant = numpy.linalg.det(array)

    decimals = f"{determinant:0.2f}".split(".")[1]

    if decimals != "00":
        print(f"{determinant:0.2f}")
    else:
        print(f"{determinant:0.1f}")

if __name__ == "__main__":
    main()

import pytest
monkeypatch = pytest.MonkeyPatch()

def test_cero(capsys):
    inputs = iter([
        "2",
        "1.1 1.1",
        "1.1 1.1",
    ])
    results = """0.0\n"""
    
    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    main()

    stdout, stderr = capsys.readouterr()
    assert results == stdout

def test_one(capsys):
    inputs = iter([
        "3",
        "1 2 3",
        "4 5 6",
        "1 2 1",
    ])
    results = """6.0\n"""
    
    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    main()

    stdout, stderr = capsys.readouterr()
    assert results == stdout