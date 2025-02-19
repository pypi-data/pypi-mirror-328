from itertools import islice


def readlines(file, *, start=0, end=None, step=None, strip=True):
    with open(file, 'r') as f:
        for line_num, line in enumerate(islice(f, start, end, step), start + 1):
            if strip:
                yield line_num, line.strip()
            else:
                yield line_num, line
