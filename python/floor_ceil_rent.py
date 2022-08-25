import numpy

def main():
    numpy.set_printoptions(legacy='1.13')

    inp = list(map(float,input().split(" ")))

    array = numpy.array(inp)

    print(numpy.floor(array))
    print(numpy.ceil(array))
    print(numpy.rint(array))


if __name__ == "__main__":
    main()

import pytest

monkeypatch = pytest.MonkeyPatch()

def test_cero(capsys):
    inputs = iter([
        "1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9",
    ])

    results = """[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]\n"""

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    main()

    stdout, stderr = capsys.readouterr()

    assert results == stdout

