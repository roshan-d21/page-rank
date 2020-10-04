#!/usr/bin/python3
import sys

pageranks = {}  # to store pageranks of nodes in v, since it is guaranteed to fit in memory

with open(sys.argv[1], 'r') as v:
    for line in v:
        node, rank = line.strip().split(', ')
        pageranks[node] = rank
# print(pageranks)

for line in sys.stdin:
    i, j, contrib = line.strip().split()

    product = float(contrib) * float(pageranks[j])

    print(i, product, sep=', ')
