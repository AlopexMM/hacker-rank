import numpy

def main():
    n,m,p = list(map(int,input().split(" ")))

    n_array = []
    m_array = []

    for _ in range(n):
        n_array.append(list(map(int,input().split(" "))))
    for _ in range(m):
        m_array.append(list(map(int,input().split(" "))))

    my_array = numpy.concatenate((n_array,m_array))

    print(my_array)

if __name__ == "__main__":
    main()

import pytest

monkeypatch = pytest.MonkeyPatch()

def test_cero(capsys):
    inputs = iter([
        "4 3 2",
        "1 2",
        "1 2", 
        "1 2",
        "1 2",
        "3 4",
        "3 4",
        "3 4", 
    ])

    results = """[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]]\n"""
    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    main()

    stdout, stderr = capsys.readouterr()

    assert results == stdout