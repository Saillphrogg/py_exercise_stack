# import modulu
from stack import Stack
import pytest

def test_simple():
    s = Stack()
    assert s.length() == 0
    s.push(1)
    assert s.length() == 1
    v = s.get()
    assert v == 1
    assert s.length() == 1
    v = s.pop()
    assert v == 1
    assert s.length() == 0

def test_adv1():
    s = Stack(int)
    assert s.length() == 0
    s.push(1)
    assert s.length() == 1
    v = s.get()
    assert v == 1
    assert s.length() == 1
    v = s.pop()
    assert v == 1
    assert s.length() == 0

def test_adv2():
    s = Stack(2)
    assert s.length() == 0
    s.push(1)
    assert s.length() == 1
    v = s.get()
    assert v == 1
    assert s.length() == 1
    v = s.pop()
    assert v == 1
    assert s.length() == 0

    # check if a function raises exception
    # see: https://docs.pytest.org/en/stable/reference/reference.html?highlight=raises#pytest.raises
    with pytest.raises(IndexError) as e:
        s.pop()

    with pytest.raises(IndexError) as e:
        s.get()

def test_eval():
    s = Stack()
    ss = eval(repr(s))
    assert ss.length() == s.length()
    s.push(1)
    ss = eval(repr(s))
    assert ss.length() == s.length()
    s.push('a')
    ss = eval(repr(s))
    assert ss.length() == s.length()
