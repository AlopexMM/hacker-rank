class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=EvenStream()):
    stream.__init__()
    for _ in range(n):
        print(stream.get_next())

def main():
    queries = int(input())
    for _ in range(queries):
        stream_name, n = input().split()
        n = int(n)
        if stream_name == "even":
            print_from_stream(n)
        else:
            print_from_stream(n, OddStream())


if __name__ == "__main__":
    main()

import pytest
monkeypatch = pytest.MonkeyPatch()

def test_cero(capsys):
    inputs = iter([
        "4",
        "odd 2",
        "even 3",
        "odd 5",
        "even 2",
    ])
    results = """1
3
0
2
4
1
3
5
7
9
0
2\n"""
    
    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    main()

    stdout, stderr = capsys.readouterr()
    assert results == stdout

# def test_one(capsys):
#     inputs = iter([
#         "5",
#         "odd 7",
#         "odd 5",
#         "odd 7",
#         "odd 2",
#         "even 6",
#     ])
#     results = """1
# 3
# 5
# 7
# 9
# 11
# 13
# 1
# 3
# 5
# 7
# 9
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 1
# 3
# 0
# 2
# 4
# 6
# 8
# 10\n"""
    
#     monkeypatch.setattr("builtins.input", lambda: next(inputs))

#     main()

#     stdout, stderr = capsys.readouterr()
#     assert results == stdout

# def test_two(capsys):
#     inputs = iter([
#         "1",
#         "even 7",
#     ])
#     results = """0
# 2
# 4
# 6
# 8
# 10
# 12\n"""
    
#     monkeypatch.setattr("builtins.input", lambda: next(inputs))

#     main()

#     stdout, stderr = capsys.readouterr()
#     assert results == stdout

# def test_three(capsys):
#     inputs = iter([
#         "5",
#         "odd 10",
#         "odd 2",
#         "odd 8",
#         "odd 8",
#         "even 1",
#     ])
#     results = """1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19
# 1
# 3
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 0\n"""
    
#     monkeypatch.setattr("builtins.input", lambda: next(inputs))

#     main()

#     stdout, stderr = capsys.readouterr()
#     assert results == stdout