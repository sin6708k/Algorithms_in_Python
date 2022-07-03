# Given two indices i and j, where i < j, find the longest increasing
# subsequence of A[j..n] in which every element is larget than A[i].
def LIS(prev: int, A: list) -> int:
    n = len(A)

    if n == 0:
        return 0
    if A[0] <= prev:
        skip = LIS(prev, A[1:])
        return skip

    skip = LIS(prev, A[1:])
    take = LIS(A[0], A[1:]) + 1
    return max(take, skip)


print(LIS(prev=0,
          A=[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6]))
