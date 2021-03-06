#!/usr/bin/python3
import sys

cur_node = None
prev_node = None
adj_list = []
unique_nodes = set()

for line in sys.stdin:
    cur_node, dest_node = line.strip().split(',')
    unique_nodes.add(cur_node)
    unique_nodes.add(dest_node)

    if cur_node == prev_node:
        adj_list.append(dest_node)
    else:
        if prev_node:
            n = len(adj_list)

            for node in adj_list:
                print(node, prev_node, 1 / n, sep='\t')

        prev_node = cur_node
        adj_list.clear()
        adj_list.append(dest_node)


if cur_node == prev_node:
    n = len(adj_list)

    for node in adj_list:
        print(node, prev_node, 1 / n, sep='\t')


with open(sys.argv[1], 'w') as v:
    n = len(unique_nodes)
    v_start = str(1 / n)

    for node in sorted(unique_nodes):
        v.write(node + ', ' + v_start + '\n')
