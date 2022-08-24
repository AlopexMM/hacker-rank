import numpy
numpy.set_printoptions(legacy='1.13')

def main():
    n,m = map(int,input().split(" "))
    print(numpy.eye(n,m))

if __name__ == "__main__":
    main()

import pytest
monkeypatch = pytest.MonkeyPatch()

def test_cero(capsys):
    inputs = iter([
        "3 3",
    ])

    results = """[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]\n"""

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    main()

    stdout, stderr = capsys.readouterr()

    assert results == stdout