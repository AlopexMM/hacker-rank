import numpy
import pytest

monkeypatch = pytest.MonkeyPatch()

def main():
    numbers = list(map(int,input().split(" ")))

    my_array = numpy.array(numbers)

    print(numpy.reshape(my_array,(3,3)))
if __name__ == "__main__":
    main()


def test_cero(capsys):
    inputs = iter(["1 2 3 4 5 6 7 8 9"])

    results = """[[1 2 3]\n [4 5 6]\n [7 8 9]]\n"""
    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    main()

    stdout, stderr = capsys.readouterr()

    assert stdout == results


