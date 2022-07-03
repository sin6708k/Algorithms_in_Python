# 두 문자열 A와 B가 주어졌을 때, A에 연산을 최소 횟수로 수행해 B로 만드는 문제를 "최소 편집" 문제라고 한다.
# A에 적용할 수 있는 연산은 총 3가지가 있으며 아래와 같다.
# 삽입: A의 한 위치에 문자 하나를 삽입한다.
# 삭제: A의 문자 하나를 삭제한다.
# 교체: A의 문자 하나를 다른 문자로 교체한다.
# 두 문자열이 주어졌을 때, 최소 편집 횟수를 구하는 프로그램을 작성하시오.
def edit_distance() -> list:
    m = len(x)
    n = len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][0] = i
    for j in range(1, n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            x_i = x[i - 1]
            y_j = y[j - 1]
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + diff(x_i, y_j))

    return dp


def diff(a: int, b: int) -> int:
    if a == b:
        return 0
    else:
        return 1


x = 'EXPONENTIAL'
y = 'POLYNOMIAL'
print(*edit_distance(), sep='\n')
