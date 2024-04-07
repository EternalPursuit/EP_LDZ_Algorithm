'''
主要是：DFS
'''
def hasPath(matrix,word):
    if len(matrix)==0:
        return False
    n = len(matrix)
    m = len(matrix[0])
    flag = [[False]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if dfs(matrix,n,m,i,j,word,0,flag):
                return True
    return False

def dfs(matrix,n,m,i,j,word,k,flag):
    if i < 0 or i >= n or j < 0 or j >= m or (matrix[i][j]!= word[k] or flag[i][j]):
        return False
    if k == len(word) - 1:
        return True
    flag[i][j] = True
    if dfs(matrix,n,m,i-1,j,word,k+1,flag) \
        or dfs(matrix,n,m,i+1,j,word,k+1,flag) \
        or dfs(matrix,n,m,i,j+1,word,k+1,flag) \
        or dfs(matrix,n,m,i,j-1,word,k+1,flag):
        return True

    flag[i][j] = False
    return False


