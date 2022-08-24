import numpy

def main():
    n, m = map(int,input().split(" "))

    arr = []

    for _ in range(n):
        inp = list(map(int,input().split(" ")))
        arr.append(inp)
    
    array = numpy.array(arr)

    sum_result = numpy.sum(array, axis=0)

    print(numpy.prod(sum_result))

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

    results = """24\n"""

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    main()

    stdout, stderr = capsys.readouterr()

    assert results == stdout