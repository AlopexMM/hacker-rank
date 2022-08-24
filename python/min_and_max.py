import numpy

def main():
    pass

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