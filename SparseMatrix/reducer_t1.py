#!/usr/bin/python3
import sys

cur_node = None
prev_node = None
adj_list = []
unique_nodes = []

for line in sys.stdin:
    cur_node, dest_node = line.strip().split(',')
    if cur_node == prev_node:
        adj_list.append(dest_node)
    else:
        if prev_node:
            n = len(adj_list)

            for node in adj_list:
                print(node, prev_node, 1 / n, sep=',')
            print(prev_node, prev_node, 0.0, sep=',')

            unique_nodes.append(prev_node)

        prev_node = cur_node
        adj_list.clear()
        adj_list.append(dest_node)

if cur_node == prev_node:
    n = len(adj_list)

    for node in adj_list:
        print(node, prev_node, 1 / n, sep=',')
    print(prev_node, prev_node, 0.0, sep=',')

    unique_nodes.append(prev_node)

with open(sys.argv[1], 'w') as v:
    n = len(unique_nodes)
    v_start = str(1 / n)
    v.write('\n'.join([v_start] * n))
