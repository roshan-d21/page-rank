import shutil
import os
count = 0
n = 0
conv = 0.5  # this value will vary for different test cases in the backend
total = 0.0


def rewrite_pagerank():
    os.remove("v")

    source = "v1"
    destination = "v"
    dest = shutil.copyfile(source, destination)


def log(total, count):
    with open('log', 'a') as f:
        f.write('=' * 25 + '\n')
        f.write("Convergence: " + str(total/count) + '\n')
        f.write('=' * 25 + '\n')


with open("v") as file1, open("v1") as file2:
    for line1, line2 in zip(file1, file2):
        count += 1
        old_pagerank = float(line1.split(",")[1])
        new_pagerank = float(line2.split(",")[1])

        total += abs(old_pagerank-new_pagerank)
        if(abs(old_pagerank-new_pagerank) < conv):
            n += 1

    if(n == count):
        print(0)
    else:
        log(total, count)
        rewrite_pagerank()
        print(1)
