import sys
n = int(sys.stdin.readline())

map = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
store = []
max_cnt = 0

def check(map):
    cnt = 0
    for i in range(n):
        row_cnt = 1
        col_cnt = 1
        for j in range(1, n):
            if map[i][j] == map[i][j-1]:
                row_cnt += 1
            else:
                row_cnt = 1
            if map[j][i] == map[j-1][i]:
                col_cnt += 1
            else:
                col_cnt = 1
            cnt = max(row_cnt, col_cnt, cnt)
    return cnt

result = 0
for i in range(n-1):
    for j in range(n-1):
        map[i][j], map[i][j+1] = map[i][j+1], map[i][j]
        result = max(check(map), result)
        map[i][j], map[i][j+1] = map[i][j+1], map[i][j]
        map[i][j], map[i+1][j] = map[i+1][j], map[i][j]
        result = max(check(map), result)
        map[i][j], map[i + 1][j] = map[i + 1][j], map[i][j]

for i in range(n-1):
    map[i][n-1], map[i+1][n-1] = map[i+1][n-1], map[i][n-1]
    result = max(check(map), result)
    map[i][n - 1], map[i + 1][n - 1] = map[i + 1][n - 1], map[i][n - 1]
    map[n-1][i], map[n-1][i+1] = map[n-1][i+1], map[n-1][i]
    result = max(check(map), result)
    map[n - 1][i], map[n - 1][i + 1] = map[n - 1][i + 1], map[n - 1][i]

print(result)