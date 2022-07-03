def coin_changing() -> list:
    n = len(coins)
    coins.sort()
    dp = [0] + [99] * money

    if money < coins[0]:
        return []

    for i in range(n):
        c_i = coins[i]
        for c in range(c_i, money + 1):
            if c - c_i >= 0:
                dp[c] = min(dp[c], dp[c - c_i] + 1)
            else:
                break

    if dp[money] >= 99:
        return []

    return dp


money = 15
coins = [1, 5, 12]
print(coin_changing())
