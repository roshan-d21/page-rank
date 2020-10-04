#!/usr/bin/python3
import sys

cur_node = None
prev_node = None
new_pr = 0.0

v1 = open(sys.argv[1], 'w')
m_out = open(sys.argv[2], 'w')

for line in sys.stdin:
    cur_node, contrib = line.strip().split(', ')

    if cur_node == prev_node:
        new_pr += float(contrib)
        m_out.write(prev_node + ', ' + str(contrib) + '\n')
    else:
        if prev_node:
            v1.write(prev_node + ', ' + str(new_pr) + '\n')
            print(prev_node, new_pr, sep=', ')
        prev_node = cur_node
        new_pr = float(contrib)
        m_out.write(prev_node + ', ' + str(contrib) + '\n')

if cur_node == prev_node:
    v1.write(prev_node + ', ' + str(new_pr) + '\n')
    print(prev_node, new_pr, sep=', ')

v1.close()
m_out.close()
