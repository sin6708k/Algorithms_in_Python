# n(2 ≤ n ≤ 100)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다.
# 각 버스는 한 번 사용할 때 필요한 비용이 있다.
# 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.
def APSP() -> list:
    dp = [[99] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][i] = 0
    for v, u, w in edges:
        dp[v][u] = w

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    continue
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    return dp


n = 5
edges = [(1, 2, 2), (1, 3, 3), (1, 4, 1), (1, 5, 10),
         (2, 4, 2),
         (3, 1, 8), (3, 4, 1), (3, 5, 1),
         (4, 5, 3),
         (5, 1, 7), (5, 2, 4)]
print(*APSP(), sep='\n')
