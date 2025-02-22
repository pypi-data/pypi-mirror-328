from csv import reader as __reader__
from sys import argv as _a
import akatool
def loader(f):
    with open(f) as f:
        for res in __reader__(f):
            yield from res
core = lambda conf, opt : ([incognito(i) for i in loader(conf)], (lambda f : f() if p else f)(__import__('subpr').lib.subpr('python -m akatool')()))
main = lambda : core(_a.pop(), len(a) > 1)
if __name__ == "__main__": main()