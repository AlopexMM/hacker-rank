import numpy

def main():
    a = numpy.array(list(map(int,input().split(" "))))
    b = numpy.array(list(map(int,input().split(" "))))

    print(numpy.inner(a,b))
    print(numpy.outer(a,b))

if __name__ == "__main__":
    main()

import pytest
monkeypatch = pytest.MonkeyPatch()

def test_cero(capsys):
    inputs = iter([
        "0 1",
        "2 3",
    ])
    results = """3
[[0 0]
 [2 3]]\n"""
    
    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    main()

    stdout, stderr = capsys.readouterr()
    assert results == stdout