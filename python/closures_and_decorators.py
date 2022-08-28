def wrapper(f):
    def fun(l):
        # complete the function
        result = []
        for phone in l:
            phone_int = int(phone)
            phone_format = str(phone_int)
            while len(phone_format) != 13:
                if len(phone_format) == 10:
                    phone_format = f"1{phone_format}"
                if len(phone_format) == 11:
                    phone_format = f"9{phone_format}"
                if len(phone_format) == 12:
                    phone_format = f"+{phone_format}"
            phone_format = f"{phone_format[0:3]} {phone_format[3:8]} {phone_format[8:13]}"
            result.append(phone_format)
        return f(result)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

def main():
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

if __name__ == '__main__':
    main()

import pytest

monkeypatch = pytest.MonkeyPatch()

def test_cero(capsys):
    inputs = iter([
        "3",
        "07895462130",
        "919875641230",
        "9195969878",
    ])

    results = """+91 78954 62130
+91 91959 69878
+91 98756 41230\n"""
    
    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    main()

    stdout, stderr = capsys.readouterr()

    assert results == stdout