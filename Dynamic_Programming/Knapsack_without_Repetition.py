# 준서가 여행에 필요하다고 생각하는 N개의 물건이 있다.
# 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다.
# 아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다.
# 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.
def knapsack() -> list:
    n = len(items)
    items.sort(key=lambda x: x[0])
    dp = [[0 for _ in range(limit + 1)] for _ in range(n)]

    for i in range(n):
        w_i = items[i][0]
        v_i = items[i][1]
        for w in range(1, limit + 1):
            if w - w_i >= 0:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - w_i] + v_i)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp


limit = 11
items = [(1, 1), (2, 6), (5, 18), (6, 22), (7, 28)]
print(*knapsack(), sep='\n')
