'''
描述
输入一个整数 n ，输出该数32位二进制表示中1的个数。其中负数用补码表示。

数据范围：−231<=n<=231−1−231<=n<=231−1
即范围为:−2147483648<=n<=2147483647−2147483648<=n<=2147483647
'''

class Solution:
    def NumberOf1(self , n: int) -> int:
        # write code here
        c = 0
        while n:
            n &= n-1
            c += 1
        return c

# java:
# public class Solution {
#     public int NumberOf1(int n) {
#         int res = 0;
#         //当n为0时停止比较
#         while(n != 0){
#             n &= n - 1;
#             res++;
#         }
#         return res;
#     }
# }
#
# c++:
# public class Solution {
#     public int NumberOf1(int n) {
#         int res = 0;
#         //当n为0时停止比较
#         while(n != 0){
#             n &= n - 1;
#             res++;
#         }
#         return res;
#     }
# }
