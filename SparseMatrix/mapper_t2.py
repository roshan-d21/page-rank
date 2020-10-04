#!/usr/bin/python3
import sys

pageranks = {}  # to store pageranks of nodes in v, since it is guaranteed to fit in memory

with open(sys.argv[1], 'r') as v:
    for line in v:
        node, rank = line.strip().split(',')
        pageranks[node] = rank

m_out = open('m_out', 'w')

for line in sys.stdin:
    node, _, contrib = line.strip().split()

    product = float(contrib) * float(pageranks[node])

    m_out.write(node + ', ' + str(product) + '\n')

m_out.close()
