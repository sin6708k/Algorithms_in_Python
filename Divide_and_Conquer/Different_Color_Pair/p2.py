def counter_clock_wise(p1: tuple, p2: tuple, p3: tuple):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])


class DifferentColorPair:
    @property
    def pairs(self):
        return self.__pairs

    def __init__(self, red: list, blue: list):
        self.__red = red
        self.__blue = blue

        self.__pairs = []

    def do(self):
        self.__pairs = self.do_recursively(self.__red, self.__blue)

    def do_recursively(self, red: list, blue: list):
        n = len(red)
        red_part1 = []
        red_part2 = []
        blue_part1 = []
        blue_part2 = []

        if n <= 0:
            raise NotImplementedError
        if n == 1:
            return [(red[0], blue[0])]

        # 2*T(n/2) + O(n^3), 재귀 함수는 전체 반복문 중에서 단 한 번만 실행되므로
        for i in range(n):
            for j in range(n):
                red_part1.clear()
                red_part2.clear()
                blue_part1.clear()
                blue_part2.clear()

                # O(n)
                for k in range(n):
                    if counter_clock_wise(red[i], blue[j], red[k]) > 0:
                        red_part1.append(red[k])
                    else:
                        red_part2.append(red[k])

                # O(n)
                for k in range(n):
                    if counter_clock_wise(red[i], blue[j], blue[k]) > 0:
                        blue_part1.append(blue[k])
                    else:
                        blue_part2.append(blue[k])

                if len(red_part1) != len(blue_part1):
                    continue
                if len(red_part1) in (0, n):
                    continue

                # 2*T(n/2)
                return self.do_recursively(red_part1, blue_part1) +\
                       self.do_recursively(red_part2, blue_part2)


def main():
    file = open('p2_input3.txt', 'r')
    n = int(file.readline())
    red_points = []
    blue_points = []

    for _ in range(n):
        line = file.readline().split()
        red_points.append(tuple(map(int, line)))
    for _ in range(n):
        line = file.readline().split()
        blue_points.append(tuple(map(int, line)))

    file.close()
    file = open('p2_output.txt', 'w')

    different_color_pair = DifferentColorPair(red_points, blue_points)
    different_color_pair.do()

    print(n, file=file)
    for pair in different_color_pair.pairs:
        print(pair[0][0], ' ', pair[0][1], ', ', pair[1][0], ' ', pair[1][1], sep='', file=file)

    file.close()


main()
