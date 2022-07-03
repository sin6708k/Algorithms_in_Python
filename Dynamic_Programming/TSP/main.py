from math import inf
from math import dist


def single_set(j: int) -> int:
    return 2 ** j


def full_set(s: int) -> int:
    return 2 ** s - 1


def elements(subset: int) -> list:
    elements_of_subset = []
    for j in range(N):
        if (subset & single_set(j)) / single_set(j) == 1:
            elements_of_subset.append(j)
    return elements_of_subset


def find_path():
    D[single_set(0), 0] = 0
    P[single_set(0), 0] = [0]

    for s in range(1, N + 1):
        for subset in range(full_set(2), full_set(s) + 1):
            if subset & single_set(0) == 0:
                continue
            elements_of_subset = elements(subset)
            for u in elements_of_subset:
                D[subset, u] = inf
                if u == 0:
                    continue
                for v in elements_of_subset:
                    if v == u:
                        continue
                    # D[subset, u] = min(D[subset, u], D[subset - single_set(u), v] + dist(V[u], V[v]))
                    if D[subset, u] > D[subset - single_set(u), v] + dist(V[v], V[u]):
                        D[subset, u] = D[subset - single_set(u), v] + dist(V[v], V[u])
                        P[subset, u] = P[subset - single_set(u), v] + [u]

    d = inf
    for u in range(N):
        # d = min(d, D[full_set(N), j] + dist(V[j], V[1]))
        if d > D[full_set(N), u] + dist(V[u], V[0]):
            d = D[full_set(N), u] + dist(V[u], V[0])
            p = P[full_set(N), u] + [0]
    return round(d, 2), p


def print_output(output: tuple):
    print(output[0], file=file)
    print(output[1].pop(0), end='', file=file)
    for v in output[1]:
        print(',', end='', file=file)
        print(v, end='', file=file)


file = open('input2.txt', 'r')
N = int(file.readline())
# V is list of all vertices
V = [tuple(map(float, file.readline().split())) for _ in range(N)]
file.close()

file = open('output.txt', 'w')
# D is dict of all distances
D = dict()
# P is dict of all paths
P = dict()
print_output(find_path())
file.close()
