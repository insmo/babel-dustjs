from babeldustjs.dustjs import extractor
import os

def datafile(name):
    return os.path.join(os.path.dirname(__file__), 'testdata', name)

def test_text():
    with open(datafile('test1.obvt')) as f:
        r = list(extractor(f, [], [], []))
        assert len(r) == 1
        lineno, funcname, message, comments = r[0]
        assert lineno == 1
        assert message == 'Hello world!'
        assert funcname is None

def test_text_singlequotes():
    with open(datafile('test8.obvt')) as f:
        r = list(extractor(f, [], [], []))
        assert len(r) == 1
        lineno, funcname, message, comments = r[0]
        assert lineno == 1
        assert message == 'Hello world!'
        assert funcname is None

def test_text_empty():
    with open(datafile('test2.obvt')) as f:
        r = list(extractor(f, [], [], []))
        assert len(r) == 1
        lineno, funcname, message, comments = r[0]
        assert lineno == 1
        assert message == ''

def test_text_and_attribute():
    with open(datafile('test3.obvt')) as f:
        r = list(extractor(f, [], [], []))
        assert len(r) == 2
        r.sort()
        lineno, funcname, message, comments = r[0]
        assert lineno == 1
        assert message == 'Hello'
        lineno, funcname, message, comments = r[1]
        assert message == 'world!'
        assert lineno == 2

def test_text_multiline():
    with open(datafile('test4.obvt')) as f:
        r = list(extractor(f, [], [], []))
        assert len(r) == 1
        lineno, funcname, message, comments = r[0]
        assert lineno == 1
        assert message == 'Hello world!'
        assert funcname is None

def test_text_multiline2():
    with open(datafile('test5.obvt')) as f:
        r = list(extractor(f, [], [], []))
        assert len(r) == 1
        lineno, funcname, message, comments = r[0]
        assert lineno == 1
        assert message == '\nHello world!\n'
        assert funcname is None

def test_text_multiline5():
    with open(datafile('test6.obvt')) as f:
        r = list(extractor(f, [], [], []))
        assert len(r) == 2
        lineno, funcname, message, comments = r[0]
        assert lineno == 1
        assert message == 'Hello world!'
        lineno, funcname, message, comments = r[1]
        assert lineno == 1
        assert message == 'Hello world!'

def test_text_multiline6():
    with open(datafile('test7.obvt')) as f:
        r = list(extractor(f, [], [], []))
        assert len(r) == 2
        lineno, funcname, message, comments = r[0]
        assert lineno == 1
        assert message == 'Hello world!'
        lineno, funcname, message, comments = r[1]
        assert lineno == 1
        assert message == 'Hello world!\n'
