def schedule():
    n = len(jobs)
    jobs.sort(key=lambda x: x[1])
    p = [0] * n
    d = [0] * n

    for i in range(n):
        s_i = jobs[i][0]
        w_i = jobs[i][2]
        for j in range(i - 1, -1, -1):
            e_j = jobs[j][1]
            if e_j <= s_i:
                p[i] = j
                break
        d[i] = max(d[i - 1], w_i + d[p[i]])

    return d


jobs = [(0, 6, 60), (1, 4, 30), (3, 5, 10), (5, 7, 30), (5, 9, 50), (7, 8, 10)]
print(schedule())
