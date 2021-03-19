n = int(input())
a, b = map(int, input().split())
m = int(input())

arr = [[0] * (n) for i in range(n)]
v = [0] * (n)


def bfs(x):
    q = [x]

    while q:

        cur = q.pop(0)
        for i in range(n):
            if arr[cur][i] == 1 and v[i] == 0:
                v[i] = v[cur] + 1
                q.append(i)


for i in range(m):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = arr[y - 1][x - 1] = 1

bfs(a - 1)
# 몇촌인지 찾기 위한 점에서 bfs 시작
# 그 점이랑 이어진 점만 몇촌인지 구하기

print(v[b - 1] if v[b - 1] else -1)