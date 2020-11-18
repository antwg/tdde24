from books import db

def match(seq, pattern) -> list:
    """
    Returns whether given sequence matches the given pattern.
    """
    if not pattern:
        return not seq
    elif isinstance(pattern[0], list): # If both are lists, compare contents.
        if isinstance(seq[0], list):
            if match(seq[0], pattern[0]) and match(seq[1:], pattern[1:]):
                return True
        else:
            return False
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
        if len(seq) == 1:
            return True
        else:
            return match(seq[1:], pattern[1:])
    elif pattern == '--':
        return True
    else:
        return False


def search(pattern, database) -> list:
    """Returns the matches of a given pattern in a given database."""
    result = []
    for book in database:
        if (match(book[0], pattern[0])
                and match(book[1], pattern[1])
                and match(book[2], pattern[2])):
            result.append(book)
    return result


"""Tests"""

test1 = search([['författare', ['&', 'zelle']],
                ['titel', ['--', 'python', '--']], ['år', '&']], db)

test2 = search(['--', ['år', 2042], '--'], db)

test3 = search(['--', ['titel', ['&', '&']], '--'], db)
