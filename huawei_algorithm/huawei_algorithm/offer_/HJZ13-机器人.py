class Solution:
    def __init__(self) -> None:
        self.threshold = None
        self.visited = None
        self.m = 0
        self.n = 0

    def movingCount(self, threshold: int, rows: int, cols: int) -> int:
        # write code here
        self.threshold = threshold
        self.visited = [[False] * cols for _ in range(rows)]
        self.m = rows
        self.n = cols
        return self.dfs(0, 0)

    def dfs(self, i: int, j: int) -> int:
        if i < 0 or j < 0 or i > (self.m - 1) or j > (self.n - 1) or self.visited[i][j] or self.threshold < (
                self.bitSum(i) + self.bitSum(j)):
            return 0

        self.visited[i][j] = True
        return 1 + self.dfs(i + 1, j) + self.dfs(i, j + 1)

    def bitSum(self,i: int):
        res = 0
        if i == 0:
            return 0
        while i:
            res += i % 10
            i //= 10
        return res

sol = Solution()
res = sol.movingCount(5,10,10)
print(res)

