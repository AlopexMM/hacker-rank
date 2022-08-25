import numpy

def main():
    n,m = map(int,input().split(" "))

    arr = []

    for _ in range(n):
        arr.append(list(map(int,input().split(" "))))

    array = numpy.array(arr)

    std = numpy.std(array)

    print(numpy.mean(array,axis=1))
    print(numpy.var(array,axis=0))
    if std > 0:
        print(f"{std:0.11f}")
    else:
        print(f"{std:0.1f}")

if __name__ == "__main__":
    main()

import pytest

monkeypatch = pytest.MonkeyPatch()

def test_cero(capsys):
    inputs = iter([
        "2 2",
        "1 2",
        "3 4",
    ])

    results = """[1.5 3.5]
[1. 1.]
1.11803398875\n"""

    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    main()
    stdout, stderr = capsys.readouterr()

    assert stdout == results

def test_cero(capsys):
    inputs = iter([
        "3 3",
        "1 1 1",
        "1 1 1",
        "1 1 1",
    ])

    results = """[1. 1. 1.]
[0. 0. 0.]
0.0\n"""

    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    main()
    stdout, stderr = capsys.readouterr()

    assert stdout == results