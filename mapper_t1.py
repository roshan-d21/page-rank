import sys

for line in sys.stdin:
    if line.startswith('#'):
        continue
    else:
        print(line, end='')
