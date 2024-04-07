#
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
#


# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         m,n = len(matrix),len(matrix[0])
#         upper,left,right,down = 0,0,n-1,m-1
#         ans = []
#         while True:
#             for i in range(left,right+1):
#                 ans.append(matrix[upper][i])
#             upper += 1
#             if upper > down: break
#             for i in range(upper,down+1):
#                 ans.append(matrix[i][right])
#             right -= 1
#             if left > right: break
#             for i in range(right,left-1,-1):
#                 ans.append(matrix[down][i])
#             down -= 1
#             if upper > down: break
#             for i in range(down,upper-1,-1):
#                 ans.append(matrix[i][left])
#             left += 1
#             if left > right:break
#         return ans

matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 矩阵转置
res0 = [*zip(*matrix)]
print(res0)
# 顺时针旋转
res1 = [*zip(*matrix[::-1])]
print(res1)
# 逆时针旋转
res2 = [*zip(*matrix)][::-1]
print(res1)
# 左右反转，实际上就是逆时针旋转之后再转置
res3 = [*zip(*res2)]
print(res3)
# 顺时针旋转再转置,就是上下翻转，这和直接matrix[::-1]是一样的
res4 = [*zip(*res1)]
print(res4)
