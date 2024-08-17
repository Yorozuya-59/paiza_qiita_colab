import math 


N, M = map(int, input().split())

for _ in range(M):
    w = int(input())

    boarder = (w + 0.5) / N - 0.5
    idx = math.ceil(boarder)
    print(N * idx if idx > 0 else N)
