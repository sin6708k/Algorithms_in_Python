# 자연수들로 이루어진 집합 X에 대해서 정수 T가 주어졌을 때,
# X의 특정 부분 집합 원소의 합이 해당 정수 T가 될 수 있는 조합이 존재하는가?
def subset_sum(X: list, T: int) -> bool:
    n = len(X)

    if T == 0:
        return True
    if T < 0 or n == 0:
        return False

    skip = subset_sum(X[1:], T)
    take = subset_sum(X[1:], T - X[0])
    return skip or take


print(subset_sum(X=[8, 6, 7, 5, 3, 10, 9],
                 T=15))
