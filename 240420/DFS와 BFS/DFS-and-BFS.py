def dfs(idx):
    global visited
    visited[idx]= True
    print(idx, end =" ")
    for next in range(1, N+1):
        if not visited[next] and grahp[idx][next]:
            dfs(next)

def bfs():
    global q, visited
    while q:
        cur = q.pop(0)
        visited[cur] = True
        print(cur, end = ' ')
        for next in range(1, N + 1) :
            if not visited[next] and grahp[cur][next]:
                visited[next] = True
                q.append(next)


N , M , V = map(int , input().split())

grahp =[ [False] * (N+1)
         for _ in range(N+1)      ]
visited =[False] *(N+1) 


for _ in range(M):
    a ,b = map (int , input().split())
    grahp[a][b]=True
    grahp[b][a]=True



dfs(V)
print()
visited =[False] *(N+1) 
q = [V]
bfs()