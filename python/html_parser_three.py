from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"{tag}")
        if attrs:
            for attr in attrs:
                print(f"-> {attr[0]} > {attr[1]}")

    
    # def handle_endtag(self, tag):
    #     print(f"{tag}")
    
    def handle_startendtag(self, tag, attrs):
        print(f"{tag}")
        if attrs:
            for attr in attrs:
                print(f"-> {attr[0]} > {attr[1]}")

def solution():
    parser = MyHTMLParser()
    n = int(input())
    for _ in range(n):
        parser.feed(input())

import pytest
monkeypatch = pytest.MonkeyPatch()

def test_one(capsys):
    inputs = iter([
        '9',
        '<head>',
        '<title>HTML</title>',
        '</head>',
        '<object type="application/x-flash"', 
        '  data="your-file.swf"', 
        '  width="0" height="0">',
        '  <!-- <param name="movie" value="your-file.swf" /> -->',
        '  <param name="quality" value="high"/>',
        '</object>',
    ])
    results = """head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high
"""
    monkeypatch.setattr('builtins.input', lambda: next(inputs))

    solution()
    stdout, stderr = capsys.readouterr()
    assert stdout == results

if __name__ == "__main__":
    solution()