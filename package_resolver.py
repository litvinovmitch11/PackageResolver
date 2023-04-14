from pprint import pprint
from parser import Parser

filename = 'test.txt'
parser = Parser(filename)
parser.make_tree()
tree = parser.get_tree()

dependencies = {}
used = {}


def find_conflicts(package, version):
    global used
    if (package, version) in used:
        return used[(package, version)]

    global tree
    global dependencies

    if len(tree[package][version]) == 0:
        used[(package, version)] = True
        return used[(package, version)]

    for name in tree[package][version]:
        if name not in dependencies:
            dependencies[name] = tree[package][version][name]
        else:
            dependencies[name] &= tree[package][version][name]

        if len(dependencies[name]) == 0:
            used[(package, version)] = False
            return used[(package, version)]

    used[(package, version)] = all([any([find_conflicts(n, v) for v in dependencies[n]]) for n in dependencies])
    return used[(package, version)]


find_conflicts('a', 1)
print(dependencies)
from pprint import pprint
from parser import Parser

filename = 'test.txt'
parser = Parser(filename)
parser.make_tree()
tree = parser.get_tree()

dependencies = {}
used = {}


def find_conflicts(package, version):
    global used
    if (package, version) in used:
        return used[(package, version)]

    global tree
    global dependencies

    if len(tree[package][version]) == 0:
        used[(package, version)] = True
        return used[(package, version)]

    for name in tree[package][version]:
        if name not in dependencies:
            dependencies[name] = tree[package][version][name]
        else:
            dependencies[name] &= tree[package][version][name]

        if len(dependencies[name]) == 0:
            used[(package, version)] = False
            return used[(package, version)]

    used[(package, version)] = all([any([find_conflicts(n, v) for v in dependencies[n]]) for n in dependencies])
    return used[(package, version)]


find_conflicts('a', 1)
print(dependencies)
