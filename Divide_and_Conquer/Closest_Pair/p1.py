def get_dist(p1: tuple, p2: tuple):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


class ClosestPair:
    @property
    def min_dist(self):
        return self.__min_dist

    def __init__(self, points):
        self.__points = points
        self.__min_dist = 20000 ** 2

    def do(self):
        # O(n log n), 가장 빠른 정렬 알고리즘의 시간 복잡도
        self.__points.sort(key=lambda p: p[0])

        self.__min_dist = 20000 ** 2
        self.do_recursively(0, len(self.__points))

    def do_recursively(self, left: int, right: int):
        n = right - left
        mid = (left + right) // 2

        # O(1)
        if n <= 1:
            raise NotImplementedError
        if n == 2:
            self.__min_dist = min(self.__min_dist,
                                  get_dist(self.__points[left], self.__points[left + 1]))
            return
        if n == 3:
            self.__min_dist = min(self.__min_dist,
                                  get_dist(self.__points[left], self.__points[left + 1]),
                                  get_dist(self.__points[left + 1], self.__points[left + 2]),
                                  get_dist(self.__points[left + 2], self.__points[left]))
            return

        # T(n/2)
        self.do_recursively(left, mid)

        # 여러 점이 같은 좌표를 가지는 경우
        if self.__min_dist == 0:
            return

        # T(n/2)
        self.do_recursively(mid, right)

        # 여러 점이 같은 좌표를 가지는 경우
        if self.__min_dist == 0:
            return

        # O(n)
        strip = []
        for i in range(left, right):
            if abs(self.__points[i][0] - self.__points[mid][0]) < self.__min_dist:
                strip.append(self.__points[i])

        # O(n log n), 가장 빠른 정렬 알고리즘의 시간 복잡도
        strip.sort(key=lambda p: p[1])

        # O(n)
        for i in range(len(strip)):
            # O(1), 최대 7번까지만 반복하므로
            for j in range(i + 1, len(strip)):
                if i + 7 <= j:
                    break
                if self.__min_dist <= strip[j][1] - strip[i][1]:
                    break
                self.__min_dist = min(self.__min_dist, get_dist(strip[i], strip[j]))


def main():
    file = open('p1_input1.txt', 'r')
    points = []

    for _ in range(int(file.readline())):
        line = file.readline().split()
        points.append(tuple(map(int, line)))

    file.close()

    closest_pair = ClosestPair(points)
    closest_pair.do()
    print(closest_pair.min_dist)


main()
