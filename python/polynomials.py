import numpy

def main():
    pol = numpy.array(list(map(float,input().split(" "))))
    x = int(input())

    print(numpy.polyval(pol,x))

if __name__ == "__main__":
    main()

import pytest
monkeypatch = pytest.MonkeyPatch()

def test_cero(capsys):
    inputs = iter([
        "1.1 2 3",
        "0",
    ])
    results = """3.0\n"""
    
    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    main()

    stdout, stderr = capsys.readouterr()
    assert results == stdout