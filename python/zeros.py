import numpy

def main():
    shape = list(map(int,input().split(" ")))
    print(numpy.zeros(tuple(shape),dtype=int))
    print(numpy.ones(tuple(shape),dtype=int))


if __name__ == "__main__":
    main()

import pytest

monkeypatch = pytest.MonkeyPatch()

def test_cero(capsys):
    inputs = iter([
        "3 3 3",
    ])

    results = """[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]\n"""

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    main()

    stdout, stderr = capsys.readouterr()

    assert results == stdout

def test_one(capsys):
    inputs = iter([
        "3 2",
    ])

    results = """[[0 0]
 [0 0]
 [0 0]]
[[1 1]
 [1 1]
 [1 1]]\n"""

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    main()

    stdout, stderr = capsys.readouterr()

    assert results == stdout