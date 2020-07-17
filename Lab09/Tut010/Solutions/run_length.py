from hypothesis import given, strategies

def encode(string):
    if not string:
        return
    c = string[0]
    n = 0
    for char in string:
        if char != c:
            yield c, n
            c = char
            n = 1
        else:
            n += 1
    yield c, n

def decode(encoded):
    string = ""
    for c, n in encoded:
        string += n*c
    return string

@given(strategies.text())
def test_round_trip(string):
    assert decode(encode(string)) == string
