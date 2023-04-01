from itertools import zip_longest


def grouper(iterable, n, *, incomplete="fill", fillvalue=None):
    """from https://docs.python.org/3/library/itertools.html#itertools-recipes
    Collect data into non-overlapping fixed-length chunks or blocks
    grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    """
    args = [iter(iterable)] * n
    if incomplete == "fill":
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == "strict":
        return zip(*args, strict=True)
    if incomplete == "ignore":
        return zip(*args)
    raise ValueError("Expected fill, strict, or ignore")


def transpose(iterable):
    """from https://docs.python.org/3/library/itertools.html#itertools-recipes
    Swap the rows and columns of the input.
    transpose([(1, 2, 3), (11, 22, 33)]) --> (1, 11) (2, 22) (3, 33)
    """
    return zip(*iterable, strict=True)
