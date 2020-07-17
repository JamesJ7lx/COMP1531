from list_exercises import *

def test_reverse():
    l = [0]
    reverse_list(l)
    assert l == [0]

    l = [-3, -2, -1, 0, 1, 2, 3]
    reverse_list(l)
    assert l == [3, 2, 1, 0, -1, -2, -3]

    # TODO Write more tests for reverse
    l = [1, 3, 3, 5, 4, 2, 2]
    reverse_list(l)
    assert l == [2, 2, 4, 5, 3, 3, 1]

    l = [0, 0, 100, 100, 5, 4, 0, 0]
    reverse_list(l)
    assert l == [0, 0, 4, 5, 100, 100, 0, 0]

def test_min():
    assert minimum([0]) == 0
    assert minimum([-3, -2, -1, 0, 1, 2, 3]) == -3
    # TODO Write more tests for minimum
    assert minimum([-99999, 99999, 0, -99998, 999998]) == -99999
    assert minimum([0, 0, 0, 0, -1, -1, -1, -1, 1, 1, 1]) == -1
    assert minimum([-0.5, -1, 0, 0.5, 1])

def test_sum():
    assert sum_list([0]) == 0
    assert sum_list([-3, -2, -1, 0, 1, 2, 3]) == 0
    # TODO Write more tests for sum
    assert sum_list([555, 555, 555, 555]) == 2220
    assert sum_list([5, -5, 1, -1, 0]) == 0