from books import db

def match(seq, pattern):
    """
    Returns whether given sequence matches the given pattern
    """

    if not pattern:
        # print('not pattern', not seq)
        return not seq
    elif isinstance(pattern[0], list):
        # print('list', pattern[0], '***', seq[0])
        if isinstance(seq[0], list):
            if match(seq[0], pattern[0]) and match(seq[1:], pattern[1:]):
                return True
        else:
            return False
    elif pattern[0] == '--':
        # print('--')
        if match(seq, pattern[1:]):
            return True
        elif not seq:
            return False
        else:
            return match(seq[1:], pattern)
    elif not seq:
        # print('not seq')
        return False
    elif pattern[0] == '&':
        # print('&', seq[0])
        return match(seq[1:], pattern[1:])
    elif seq[0] == pattern[0]:
        # print(seq[0], ' = ', seq[0])
        if len(seq) == 1:
            # print('len1')
            return True
        else:
            return match(seq[1:], pattern[1:])
    else:
        # print('else')
        return False


def search(pattern, database):
    result = []
    for book in database:
        # print('book', book)
        if match(book, pattern):
            # print('match')
            result.append(book)
    return result

# print(search([['författare', ['&', 'zelle']], ['titel', ['--', 'python', '--']], ['år', '&']], db))
