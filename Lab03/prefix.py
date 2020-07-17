def prefix_search(dictionary, key_prefix):
    '''
    Given a dictionary (with strings for keys) and a string, returns a new dictionary containing only the keys (and their corresponding values) for which the string is a prefix. If the string is not a prefix for any key, a KeyError is raised.

    For example,
    >>> prefix_search({"ac": 1, "ba": 2, "ab": 3}, "a")
    {'ac': 1, 'ab': 3}
    '''
    d = {i : dictionary[i] for i in dictionary if i.startswith(key_prefix)}

    if d:
        return d
    raise KeyError('The string is not a prefix for any key')

    if _name_ == '__main__':
        print(prefix_search({"ac": 1, "ba": 2, "ab": 3}, "a"))
