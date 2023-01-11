def dfs(x, y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and ch[nx][ny] == 0 and g[nx][ny] == 1:
            ch[nx][ny] = 1
            cnt += 1
            dfs(nx, ny)

n = int(input())
g = [list(map(int, list(input()))) for _ in range(n)]
ch = [[0] * n for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
l = []

for i in range(n):
    for j in range(n):
        if g[i][j] == 1 and ch[i][j] == 0:
            cnt = 1
            ch[i][j] = 1
            dfs(i, j)
            l.append(cnt)
l.sort()
print(len(l))
print(*l, sep = '\n')