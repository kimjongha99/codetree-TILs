from collections import deque

def find_pos(board):
    pos = {}
    for i, row in enumerate(board):
        for j, elem in enumerate(row):
            if elem in { 'L' , 'R', 'B'}:
                pos[elem] = (i,j)
    return pos['L'] , pos['R'] , pos['B']



def bfs(start_pos, block_pos, target_pos, board):
    new_dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우 이동에 대한 행 변화
    new_dy = [0, 0, -1, 1]  # 상, 하, 좌, 우 이동에 대한 열 변화

    queue  = deque([(start_pos[0],start_pos[1],0)])
    visited = [[False] * 10 for _ in range(10)]
    visited[start_pos[0]][start_pos[1]] = True
    
    while queue:
        x,y,count = queue.popleft()

        if (x,y) == target_pos:
            return count
        
        for i in range(4):
            nx = x + new_dx[i]
            ny = y + new_dy[i]

            if 0<=nx <10 and 0<=ny<10 and not visited[nx][ny] and board[nx][ny] !='R':
                visited[nx][ny] =True
                if board[nx][ny] =='.':
                    new_count = count + 1
                else:
                    new_count = count
                
                queue.append((nx, ny, new_count))




n = 10
board = [
    input()
    for _ in range(n)
]


start_pos , block_pos, target_pos =  find_pos(board)

short_path_length = bfs(start_pos, block_pos, target_pos, board)


print(short_path_length)