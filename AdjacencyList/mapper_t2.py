#!/usr/bin/python3
import sys

pageranks = {}  # to store pageranks of nodes in v, since it is guaranteed to fit in memory

with open(sys.argv[1], 'r') as v:
    for line in v:
        node, rank = line.strip().split(',')
        pageranks[node] = rank

for line in sys.stdin:
    node, adj_list = line.strip().split('\t')
    adj_list = adj_list.split(',')
    out_num = len(adj_list)     # number of outgoing links

    print(node, '0.0', sep=',')    # contribution of from node = 0.0
    for out_link in adj_list:
        out_link_contrib = float(pageranks[node]) / out_num
        print(out_link, str(out_link_contrib), sep=',')
