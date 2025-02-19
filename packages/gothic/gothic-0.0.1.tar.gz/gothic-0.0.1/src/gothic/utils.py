from collections import defaultdict
import sys
from functools import reduce

generator = type(x for x in [1])


def listify(x):
    if type(x) is not list:
        return [x]
    return x


class DictQueue:
    def __init__(self, *args, **kwargs):
        self.DQ = defaultdict(list, dict(*args, **kwargs))

    def push(self, k, v):
        self.DQ[k] += [v]

    def __getitem__(self, k):
        if not k in self:
            raise KeyError
        queue = self.DQ[k]
        item = queue[0]
        self.DQ[k] = queue[1:]
        if len(self.DQ[k]) == 0:
            del self.DQ[k]
        return item

    def __contains__(self, k):
        return k in self.DQ


class infinitely_many_of:
    def __init__(self, x):
        self.x = x

    def __getitem__(self, i):
        # should return the finite range of the slice if it is definite,
        # but currently returns an infinite amount no matter what
        if isinstance(i, slice):
            return self
        return self.x

    def __iter__(self):
        while True:
            yield self.x

    def __contains__(self, k):
        return k == self.x

    def __len__(self):
        # close enough lmfao
        return sys.maxsize


def splitter(f, L, keep_delimiter=False):
    for i, x in enumerate(L):
        if f(x):
            return (
                [L[:i]]
                + ([[L[i]]] if keep_delimiter else [])
                + splitter(f, L[i + 1 :], keep_delimiter=keep_delimiter)
            )
    return [L]


def intersperse(x, L):
    return list(reduce(lambda l, r: l + r, zip(L, infinitely_many_of(x))))[:-1]


def flatten(L: list) -> list:
    flatL = []
    for x in L:
        if type(x) is list:
            x = flatten(x)
            flatL += x
        else:
            flatL.append(x)
    return flatL


def plus(l, r):
    return l + r


def window_iter(n: int, L: list, increment_by=None):
    assert n > 0
    increment_by = n if increment_by is None else increment_by
    assert increment_by > 0
    i = 0
    while i + (n - 1) < len(L):
        yield L[i : i + n]
        i += increment_by
    remainder = L[i:]
    if len(remainder) > 0:
        yield remainder + [None] * (n - len(remainder))


def find(f, L):
    for x in L:
        if f(x):
            return x
    return None


class Infinity:
    def __init__(self) -> None:
        pass

    def __gt__(self, other):
        return True

    def __sub__(self, other):
        return self


INFINITY = Infinity()
