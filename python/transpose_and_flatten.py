import numpy

def main():
    n, m = list(map(int,input().split(" ")))

    my_array = []

    for _ in range(n):
        my_array.append(list(map(int,input().split(" "))))
    
    my_array = numpy.array(my_array)

    print(my_array.transpose())
    print(my_array.flatten())

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

    results = """[[1 3]
 [2 4]]
[1 2 3 4]\n"""

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    main()

    stdout, stderr = capsys.readouterr()

    assert stdout == results
