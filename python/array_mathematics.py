import numpy

def main():
    """You are given two integer arrays, A and B of dimensions N x M.
        Your task is to perform the following operations:

        Add ( N + M )
        Subtract ( N - M )
        Multiply ( N * M )
        Integer Division ( N / M )
        Mod ( N % M )
        Power ( N ** M )
        
        The first line contains two space separated integers, N and M.
        The next N lines contains M space separated integers of array A.
        The following N lines contains M space separated integers of array B."""

    n, m = map(int,input().split(" "))

    a = []
    b = []
    for _ in range(n):
        a.append(numpy.array(list(map(int, input().split(" ")))))
    for _ in range(n):
        b.append(numpy.array(list(map(int, input().split(" ")))))

    final_a = numpy.array(a)
    final_b = numpy.array(b)
    
    print(final_a + final_b)
    print(final_a - final_b)
    print(final_a * final_b)
    print(final_a // final_b)
    print(final_a % final_b)
    print(final_a ** final_b)
        
    




if __name__ == "__main__":
    main()

import pytest

monkeypatch = pytest.MonkeyPatch()

def test_cero(capsys):
    inputs = iter([
        "1 4",
        "1 2 3 4",
        "5 6 7 8",
    ])

    results = """[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]]\n"""

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    main()

    stdout, stderr = capsys.readouterr()

    assert results == stdout

def test_one(capsys):
    inputs = iter([
        "2 4",
        "1 2 3 4",
        "1 2 3 4",
        "5 6 7 7",
        "5 6 7 7",
    ])

    results = """[[ 6  8 10 11]
 [ 6  8 10 11]]
[[-4 -4 -4 -3]
 [-4 -4 -4 -3]]
[[ 5 12 21 28]
 [ 5 12 21 28]]
[[0 0 0 0]
 [0 0 0 0]]
[[1 2 3 4]
 [1 2 3 4]]
[[    1    64  2187 16384]
 [    1    64  2187 16384]]\n"""

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    main()

    stdout, stderr = capsys.readouterr()

    assert results == stdout