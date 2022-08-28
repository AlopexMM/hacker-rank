import operator

def person_lister(f):
    def inner(people):
        from operator import itemgetter
        for p in range(len(people)):
            people[p][2] = int(people[p][2])
        people.sort(key=operator.itemgetter(2))
        for person in people:
            yield f(person)
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

def main():
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

if __name__ == '__main__':
    main()

import pytest

monkeypatch = pytest.MonkeyPatch()

def test_cero(capsys):
    inputs = iter([
        "3",
        "Mike Thomson 20 M",
        "Robert Bustle 32 M",
        "Andria Bustle 30 F",
    ])

    results = """Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle\n"""
    
    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    main()

    stdout, stderr = capsys.readouterr()

    assert results == stdout

def test_one(capsys):
    inputs = iter([
        "6",
        "Blossom Michael 9 F",
        "Bubbles Kevin 666666666666666 F",
        "Buttercup Jake 4444444444444444444444444444444444444444444444444444444444444444 F",
        "Michael Blossom 8888 M",
        "Kevin Bubbles 7777777 M",
        "Jake Buttercup 555555555555555555555555555555 M",
    ])

    results = """Ms. Blossom Michael
Mr. Michael Blossom
Mr. Kevin Bubbles
Ms. Bubbles Kevin
Mr. Jake Buttercup
Ms. Buttercup Jake\n"""
    
    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    main()

    stdout, stderr = capsys.readouterr()

    assert stdout == results