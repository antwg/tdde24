from books import db

def match(seq, pattern) -> list:
    """
    Returns whether given sequence matches the given pattern.
    """
    if not pattern:
        return not seq

    elif pattern[0] == '--':
        if match(seq, pattern[1:]):
            return True
        elif not seq:
            return False
        else:
            return match(seq[1:], pattern)

    elif not seq:
        return False

    elif pattern[0] == '&':
        return match(seq[1:], pattern[1:])

    elif seq[0] == pattern[0]:
        #Check if the last element in the list is correct
        if len(seq) == 1:
            return True
        else:
            return match(seq[1:], pattern[1:])

    elif isinstance(pattern[0], list): # If both are lists, compare contents.
        if isinstance(seq[0], list):
            if match(seq[0], pattern[0]) and match(seq[1:], pattern[1:]):
                return True

        else:
            return False
    else:
        return False


def search(pattern, database) -> list:
    """Returns the matches of a given pattern in a given database."""
    result = []
    for book in database:
        if match(book, pattern):
            result.append(book)
    return result


def tests():
    """Tests"""
    test1 = search([['författare', ['&', 'zelle']],
                    ['titel', ['--', 'python', '--']], ['år', '&']], db)

    assert test1 == [[['författare', ['john', 'zelle']], ['titel',
    ['python', 'programming', 'an', 'introduction',
    'to', 'computer', 'science']], ['år', 2010]],
    [['författare', ['john', 'zelle']], ['titel',
    ['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']],
    ['år', 2009]]]

    test2 = search(['--', ['år', 2042], '--'], db)

    assert test2 == []

    test3 = search(['--', ['titel', ['&', '&']], '--'], db)

    assert test3 == [[['författare', ['armen', 'asratian']], ['titel',
    ['diskret', 'matematik']], ['år', 2012]]]

    test4 = search([[], [], []], db)
    assert test4 == []
    # print(test4)

    test5 = search(['--', '--', '--'], db)
    assert test5 == db

    print('Passed all tests')
tests()
