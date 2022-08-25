import numpy

def main():
    n,m = map(int,input().split(" "))

    arr = []

    for _ in range(n):
        arr.append(list(map(int,input().split(" "))))
    
    array = numpy.array(arr)

    min = numpy.min(array,axis=1)

    print(numpy.max(min))

if __name__ == "__main__":
    main()

import pytest
monkeypatch = pytest.MonkeyPatch()

def test_cero(capsys):
    inputs = iter([
        "4 2",
        "2 5",
        "3 7",
        "1 3",
        "4 0",
    ])

    results = """3\n"""

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    main()

    stdout, stderr = capsys.readouterr()

    assert results == stdout