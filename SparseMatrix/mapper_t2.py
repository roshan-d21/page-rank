#!/usr/bin/python3
import sys
from subprocess import Popen, PIPE

pageranks = {}  # to store pageranks of nodes in v, since it is guaranteed to fit in memory

with open(sys.argv[1], 'r') as v:
    for line in v:
        node, rank = line.strip().split(',')
        pageranks[node] = rank

for line in sys.stdin:
    node, _, contrib = line.strip().split()

    product = float(contrib) * float(pageranks[node])

    print(node, product, sep=', ')
