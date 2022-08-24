from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        lines = data.split("\n")
        if len(lines) > 1:
            print(f">>> Multi-line Comment\n{data}")
        else:
            print(f">>> Single-line Comment\n{data}")
    
    def handle_data(self, data):
        if data != "\n":
            print(f">>> Data\n{data}")

def main():
    html = ""
    n = int(input())
    for _ in range(n):
        html += input().rstrip()
        html += "\n"
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()

import pytest

monkeypatch = pytest.MonkeyPatch()

def test_one(capsys):
    inputs = iter([
        "4",
        "<!--[if IE 9]>IE9-specific content",
        "<![endif]-->",
        "<div> Welcome to HackerRank</div>",
        "<!--[if IE 9]>IE9-specific content<![endif]-->",
    ])
    results = """>>> Multi-line Comment
[if IE 9]>IE9-specific content
<![endif]
>>> Data
 Welcome to HackerRank
>>> Single-line Comment
[if IE 9]>IE9-specific content<![endif]
"""
    monkeypatch.setattr("builtins.input",lambda: next(inputs))

    main()

    stdout, stderr = capsys.readouterr()
    assert stdout == results



if __name__ == "__main__":
    main()
    