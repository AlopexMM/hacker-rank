import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    old_elem = elem
    old_tag = elem.tag
    level += 1
    if len(elem) > 0:
        level += 1
        while True:
            for e in elem:
                if len(e) > 0 and e.tag != old_tag:
                    elem = e
                    level += 1
                    old_tag = e.tag
            if elem == old_elem:
                break
            else:
                old_elem = elem
    maxdepth = level


        
def main():
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

import pytest

monkeypatch = pytest.MonkeyPatch()

def test_one(capsys):
    inputs = iter([
        "6",
        "<feed xml:lang='en'>",
        "    <title>HackerRank</title>",
        "    <subtitle lang='en'>Programming challenges</subtitle>",
        "    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>",
        "    <updated>2013-12-25T12:00:00</updated>",
        "</feed>"
    ])
    result = "1\n"
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    main()
    stdout, stderr = capsys.readouterr()
    assert stdout == result

def test_two(capsys):
    inputs = iter([
        "11",
        "<feed xml:lang='en'>",
        "   <title>HackerRank</title>",
        "   <subtitle lang='en'>Programming challenges</subtitle>",
        "   <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>",
        "   <updated>2013-12-25T12:00:00</updated>",
        "   <entry>",
        "       <author gender='male'>Harsh</author>",
        "       <question type='hard'>XML 1</question>",
        "       <description type='text'>This is related to XML parsing</description>",
        "   </entry>",
        "</feed>",
    ])
    result = "2\n"
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    main()
    stdout, stderr = capsys.readouterr()
    assert stdout == result

def test_three(capsys):
    inputs = iter([
        "16",
        "<feed xml:lang='en'>",
        "<title>HackerRank</title>",
        "<subtitle lang='en'>Programming challenges</subtitle>",
        "<link rel='alternate' type='text/html' href='http://hackerrank.com/'/>",
        "<updated>2013-12-25T12:00:00</updated>",
        "<entry>",
        "    <author gender='male'>Harsh</author>",
        "    <question type='hard'>XML 1</question>",
        "    <description type='text'>This is related to XML parsing</description>",
        "</entry>",
        "<entry>",
        "    <author gender='male'>Harsh</author>",
        "    <question type='medium'>XML 2</question>",
        "    <description type='text'>This is related to XML parsing</description>",
        "</entry>",
        "</feed>",
    ])
    result = "2\n"
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    main()
    stdout, stderr = capsys.readouterr()
    assert stdout == result

def test_four(capsys):
    inputs = iter([
        "1",
        "<feed xml:lang='en'/>",
    ])
    result = "0\n"
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    main()
    stdout, stderr = capsys.readouterr()
    assert stdout == result


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
#     xml = """<feed xml:lang='en'>
# <title>HackerRank</title>
# <subtitle lang='en'>Programming challenges</subtitle>
# <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
# <updated>2013-12-25T12:00:00</updated>
# <entry>
#     <author gender='male'>Harsh</author>
#     <question type='hard'>XML 1</question>
#     <description type='text'>This is related to XML parsing</description>
# </entry>
# <entry>
#     <author gender='male'>Harsh</author>
#     <question type='medium'>XML 2</question>
#     <description type='text'>This is related to XML parsing</description>
# </entry>
# </feed>"""
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)