from math import atan2
from math import asin
from math import sqrt
from math import degrees


center: tuple = None
polar_ranges = []
overlap = {}
overlap_inverse = {}


def circle_to_polar_range(cartesian: tuple) -> tuple:
    mid_angle = atan2(cartesian[1] - center[1], cartesian[0] - center[0])
    diff_angle = asin(cartesian[2] / sqrt(pow(center[0] - cartesian[0], 2) +
                                          pow(center[1] - cartesian[1], 2)))
    return degrees(mid_angle - diff_angle), degrees(mid_angle + diff_angle)


def load_file():
    global center
    global polar_ranges

    file = open('input.txt', 'r')
    line = file.readline()
    center = tuple(map(float, line.split()))
    while True:
        line = file.readline()
        if not line:
            break
        polar_ranges.append(circle_to_polar_range(tuple(map(float, line.split()))))
    file.close()


def check_overlap():
    global polar_ranges
    global overlap
    global overlap_inverse
    n = len(polar_ranges)

    for i in range(n):
        overlap[i] = []
        overlap_inverse[i] = []
        for e in range(2):
            overlap[i].append([])
            overlap_inverse[i].append([])

    # O(n²)
    for i in range(n):
        for e in range(2):
            for j in range(n):
                if polar_ranges[i][e] < polar_ranges[j][0]:
                    continue
                if polar_ranges[j][1] < polar_ranges[i][e]:
                    continue
                # polar range의 시작점 또는 끝점과 겹치는 polar range들을 전부 구한다.
                overlap[i][e].append(j)
                overlap_inverse[j][e].append(i)


def shot() -> int:
    global overlap
    global overlap_inverse
    n = len(overlap)

    # base case
    if n == 0:
        return 0

    selected_i = 0
    selected_e = 0
    max_overlap_count = 0

    # O(n)
    for i in overlap.keys():
        for e in range(2):
            overlap_count = len(overlap[i][e])
            if max_overlap_count < overlap_count:
                selected_i = i
                selected_e = e
                max_overlap_count = overlap_count

    # 모든 polar range가 서로 다른 polar range와 겹치지 않으면
    if max_overlap_count == 1:
        return n

    # O(n²)
    for j in overlap[selected_i][selected_e][:]:
        del overlap[j]
        for e in range(2):
            for k in overlap_inverse[j][e]:
                if k in overlap.keys():
                    overlap[k][e].remove(j)
        del overlap_inverse[j]

    return shot() + 1


load_file()
check_overlap()
print(shot())
