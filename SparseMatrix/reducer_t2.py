#!/usr/bin/python3
import sys

cur_node = None
prev_node = None
new_pr = 0.0

with open('m_out', 'r') as m_out, open('v1', 'w') as v1:
    for line in m_out:
        cur_node, contrib = line.strip().split(',')

        if cur_node == prev_node:
            new_pr += float(contrib)
        else:
            if prev_node:
                v1.write(prev_node + ', ' + str(new_pr) + '\n')
            prev_node = cur_node
            new_pr = float(contrib)

    if cur_node == prev_node:
        v1.write(prev_node + ', ' + str(new_pr) + '\n')
