"""
It must start with a # symbol
It can have 3 or 6 digits
Each digit is in the range of 0 to F (1,2,3,4,5,6,7,8,9,0,A,B,C,D,E and F)
A - F letters can be lower case (a,b,c,d,e and f are also valid digits)
"""
import re

def solution():
    pattern = re.compile("(#[0-9abcdefABCDEF]{3,6})")
    pattern_begin = re.compile("{$")
    pattern_end = re.compile("}$")
    # Comment lines object when you finish testing
    lines = []
    begin_end = ""
    n = int(input())
    for _ in range(n):
        tmp = input()
        begin_match = pattern_begin.search(tmp)
        end_match = pattern_end.search(tmp)
        if (begin_end == "" or begin_end == "}") and begin_match:
            begin_end = "{"
        elif begin_end == "{" and end_match == None:
                groups = pattern.finditer(tmp)
                for match in groups:
                    # If you finish testing the code comment the next line
                    lines.append(match.group(0))
                    # If you finish testing uncomment the next line
                    # print(match.group(0))
        elif begin_end == "{" and end_match:
            begin_end = "}"
    # Comment the next line when you finish testing
    return lines

import pytest

monkeypatch = pytest.MonkeyPatch()

def test_one():
    inputs = iter([
        "11",
        "#BED",
        "{",
        "    color: #FfFdF8; background-color:#aef;",
        "    font-size: 123px;",
        "    background: -webkit-linear-gradient(top, #f9f9f9, #fff);",
        "}",
        "#Cab",
        "{",
        "    background-color: #ABC;",
        "    border: 2px dashed #fff;",
        "}",
    ])
    results = [
        "#FfFdF8",
        "#aef",
        "#f9f9f9",
        "#fff",
        "#ABC",
        "#fff",
    ]
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    output = solution()
    monkeypatch.undo()
    assert output == results

def test_two():
    inputs = iter([
        "24",
        ".custom-file-input::-webkit-file-upload-button {",
        "visibility: hidden;",
        "}",
        ".custom-file-input::before {",
        "content: 'Select some files';",
        "display: inline-block;",
        "background: -webkit-linear-gradient(top, #f9f9f9, #e3e3e3);",
        "border: 1px solid #999;",
        "border-radius: 3px;",
        "padding: 5px 8px;",
        "outline: none;",
        "white-space: nowrap;",
        "-webkit-user-select: none;",
        "cursor: pointer;",
        "text-shadow: 1px 1px #fff;",
        "font-weight: 700;",
        "font-size: 10pt;",
        "}",
        ".custom-file-input:hover::before {",
        "border-color: black;",
        "}",
        ".custom-file-input:active::before {",
        "background: -webkit-linear-gradient(top, #e3e3e3, #f9f9f9);",
        "}",
    ])
    results = [
        "#f9f9f9",
        "#e3e3e3",
        "#999",
        "#fff",
        "#e3e3e3",
        "#f9f9f9",
    ]
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    output = solution()
    monkeypatch.undo()
    assert output == results

if __name__ == "__main__":
    solution()