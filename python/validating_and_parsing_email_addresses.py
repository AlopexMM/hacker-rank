"""
A valid email address meets the following criteria:

    It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
    The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
    The domain and extension contain only English alphabetical characters.
    The extension is 1, 2, or 3 characters in length.
Example
7
dheeraj <dheeraj-234@gmail.com>
crap <itsallcrap>
harsh <harsh_1234@rediff.in>
kumal <kunal_shin@iop.az>
mattp <matt23@@india.in>
harsh <.harsh_1234@rediff.in>
harsh <-harsh_1234@rediff.in>

Expected
dheeraj <dheeraj-234@gmail.com>
harsh <harsh_1234@rediff.in>
kumal <kunal_shin@iop.az>
"""

import re
from email.utils import parseaddr, formataddr



def validating_and_parsing_email():
    # Comment result list when you finish
    result = []
    # My solution
    n = int(input())
    pattern = re.compile("^[a-z][\w\-\d\.]*@[a-z]+\.[a-z]{0,3}$")
    for _ in range(n):
        email_parse = parseaddr(input())
        if email_parse[1] != "" and email_parse[0] != "":
            match = pattern.match(email_parse[1])
            if match != None:
                # Uncomment print when you finish
                # print(formataddr(email_parse))
                result.append(formataddr(email_parse))
    # Comment this line when you finish
    return result

if __name__ == "__main__":
    validating_and_parsing_email()

# Pytest library
import pytest
from io import StringIO

# Tests
monkeypatch = pytest.MonkeyPatch()

def test_main_one():
    monkeypatch = pytest.MonkeyPatch()
    results = ["DEXTER <dexter@hotmail.com>"]
    inputs = iter([
        "2",
        "DEXTER <dexter@hotmail.com>",
        "VIRUS <virus!@variable.:p>"
    ])
    monkeypatch.setattr('builtins.input',lambda: next(inputs))
    output = validating_and_parsing_email()
    monkeypatch.undo()
    assert output == results

def test_main_two():
    results = [
        "dheeraj <dheeraj-234@gmail.com>",
        "harsh <harsh_1234@rediff.in>",
        "kumal <kunal_shin@iop.az>"
        ]
    inputs = iter([
        "7",
        "dheeraj <dheeraj-234@gmail.com>",
        "crap <itsallcrap>",
        "harsh <harsh_1234@rediff.in>",
        "kumal <kunal_shin@iop.az>",
        "mattp <matt23@@india.in>",
        "harsh <.harsh_1234@rediff.in>",
        "harsh <-harsh_1234@rediff.in>"
    ])
    monkeypatch.setattr('builtins.input',lambda: next(inputs))
    output = validating_and_parsing_email()
    monkeypatch.undo()
    assert output == results

def test_main_three():
    results = [
        "vineet <vineet.iitg@gmail.com>",
        "vineet <vineet.iitg@gmail.co>",
        "vineet <vineet.iitg@gmail.c>"
        ]
    inputs = iter([
        "3",
        "vineet <vineet.iitg@gmail.com>",
        "vineet <vineet.iitg@gmail.co>",
        "vineet <vineet.iitg@gmail.c>"
    ])
    monkeypatch.setattr('builtins.input',lambda: next(inputs))
    output = validating_and_parsing_email()
    monkeypatch.undo()
    assert output == results

def test_main_four():
    monkeypatch = pytest.MonkeyPatch()
    results = [    
        "this <is@valid.com>",
        "this <is_it@valid.com>",
        ]
    inputs = iter([
        "4",
        "this <is@valid.com>",
        "this <is_som@radom.stuff>",
        "this <is_it@valid.com>",
        "this <_is@notvalid.com>",
    ])
    monkeypatch.setattr('builtins.input',lambda: next(inputs))
    output = validating_and_parsing_email()
    monkeypatch.undo()
    assert output == results

def test_main_five():
    monkeypatch = pytest.MonkeyPatch()
    results = ["shashank <shashank@mail.moc>"]
    inputs = iter([
        "6",
        "shashank <shashank@9mail.com>",
        "shashank <shashank@gmail.9om>",
        "shashank <shashank@gma_il.com>",
        "shashank <shashank@mail.moc>",
        "shashank <shashank@company-mail.com>",
        "shashank <shashank@companymail.c_o>",
    ])
    monkeypatch.setattr('builtins.input',lambda: next(inputs))
    output = validating_and_parsing_email()
    monkeypatch.undo()
    assert output == results