import sys

cur_node = None
prev_node = None
contrib_sum = 0

for line in sys.stdin:
    cur_node, contrib = line.strip().split(',')

    if cur_node == prev_node:
        contrib_sum += float(contrib)
    else:
        if prev_node:
            new_pr = 0.15 + 0.85 * contrib_sum
            round(new_pr, 5)
            print(prev_node, new_pr, sep=', ')
        prev_node = cur_node
        contrib_sum = 0

if cur_node == prev_node:
    new_pr = 0.15 + 0.85 * contrib_sum
    round(new_pr, 5)
    print(prev_node, new_pr, sep=', ')
