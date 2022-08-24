from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        if attrs:
            for attr in attrs:
                print(f"-> {attr[0]} > {attr[1]}")

    
    def handle_endtag(self, tag):
        print(f"End   : {tag}")
    
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        if attrs:
            for attr in attrs:
                print(f"-> {attr[0]} > {attr[1]}")

def solution():
    parser = MyHTMLParser()
    n = int(input())
    for _ in range(n):
        parser.feed(input())

# Tests code
import pytest

monkeypatch = pytest.MonkeyPatch()

def test_one(capsys):
    inputs = iter([
        "2",
        "<html><head><title>HTML Parser - I</title></head>",
        "<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>",
    ])
    results = """Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-> data-modal-target > None
-> class > 1
Start : h1
End   : h1
Empty : br
End   : body
End   : html
"""
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    
    solution()
    stdout, stderr = capsys.readouterr()
    assert stdout == results

def test_two(capsys):
    inputs = iter([
        '11',
        '<!--[if !IE 6]><!-->',
        '  <link rel="stylesheet" type="text/css" media="screen, projection" href="REGULAR-STYLESHEET.css" />',
        '<!--<![endif]-->',
        '',
        '<!--[if gte IE 7]>',
        '  <link rel="stylesheet" type="text/css" media="screen, projection" href="REGULAR-STYLESHEET.css" />',
        '<![endif]-->',
        '',
        '<!--[if lte IE 6]>',
        '  <link rel="stylesheet" type="text/css" media="screen, projection" href="http://universal-ie6-css.googlecode.com/files/ie6.0.3.css" />',
        '<![endif]-->',
    ])
    results = """Empty : link
-> rel > stylesheet
-> type > text/css
-> media > screen, projection
-> href > REGULAR-STYLESHEET.css
"""
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    
    solution()
    stdout, stderr = capsys.readouterr()
    assert stdout == results

if __name__ == "__main__":
    solution()