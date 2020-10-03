import sys

for line in sys.stdin:
    if line.startswith('#'):
        continue
    else:
        print(",".join(line.strip().split("\t")))
