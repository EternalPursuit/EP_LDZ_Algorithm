while True:
    try:
        m,n = map(int,input().split())
        maze = [list(map(int,input().split())) for _ in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        flag = False
        res = []
        def dfs(maze,visited,i,j,res=[]):
            # if visited[i][j]==True and maze[i][j]==1 and (i <0 or j <0 or i >= m or j >= n):
            if i < 0 or i >= m or j < 0 or j >=n or visited[i][j] or maze[i][j] == 1:
                return
            res.append((i, j))
            visited[i][j] = True
            if (i,j) == (len(maze)-1,len(maze[0])-1):
                [print(item) for item in res]
                return
            dfs(maze,visited,i+1,j,res)
            dfs(maze,visited,i,j-1,res)
            dfs(maze,visited,i-1,j,res)
            dfs(maze,visited,i,j+1,res)
            res.pop()
            visited[i][j] = False
        dfs(maze,visited,0,0,[])






    except:
        break