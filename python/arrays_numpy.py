import numpy
import pytest

monkeypatch = pytest.MonkeyPatch()

def arrays(arr):
    arr.reverse()
    r = numpy.array(arr, float)
    return r

def main():
    arr = input().strip().split(' ')
    result = arrays(arr)
    print(result)

if __name__ == "__main__":
    main()


def test_one(capsys):
    inputs = iter([
        "1 2 3 4 -8 -10",
    ])

    result = "[-10.  -8.   4.   3.   2.   1.]\n"

    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    main()
    stdout, stderr = capsys.readouterr()

    assert result == stdout
