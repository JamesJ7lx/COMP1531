from count import count_char

def test_empty():
    assert count_char("") == {}

def test_simple():
    assert count_char("abc") == {"a": 1, "b": 1, "c": 1}
    assert count_char("123") == {"1": 1, "2": 1, "3": 1}
    assert count_char("khj") == {"k": 1, "h": 1, "j": 1}
    assert count_char("#^@") == {"#": 1, "^": 1, "@": 1}


def test_double():
    assert count_char("hh") == {"h": 2}
    assert count_char("aa") == {"a": 2}
    assert count_char("@@") == {"@": 2}
    assert count_char("99") == {"9": 2}


def test_triple():
    assert count_char("aaabbb") == {"a": 3, "b": 3}
    assert count_char("$$$###") == {"$": 3, "#": 3}
    assert count_char("oooOO!!!") == {"o": 3, "O": 2, "!": 3}

def test_random():
    assert count_char("BBBb  ") == {"B": 3, "b": 1, " ": 2}
    assert count_char("YeEEYeEl@@YYeee") == {"Y": 4, "e": 5, "E": 3, "l": 1, "@": 2}

    