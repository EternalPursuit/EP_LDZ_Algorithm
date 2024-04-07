class Solution:
    def Permutation(self , ss: str) -> List[str]:
#         # write code here
#         # res = []
#         # length = len(ss)
#         # if length <= 1:
#         #     return [ss]
#         # for i in range(length):
#         #     first_str = ss[i]
#         #     for temp_ in self.Permutation(ss[:i]+ss[i+1:]):
#         #         tmp = first_str + temp_
#         #         if tmp not in res:
#         #             res.append(tmp)
#         # return res



        tmp = list(ss)
        tmp.sort()
        str_target = ''.join(tmp)
        vis = [0]*len(ss)
        res = []
        temp = ''
        self.recursion(res,str_target,temp,vis)
        return res

    def recursion(self,res,str_temp,temp,vis):
        if len(temp) == len(str_temp):
            res.append(temp)
            return
        for i in range(len(str_temp)):
            if vis[i] == 1:
                continue
            if i > 0 and str_temp[i-1] == str_temp[i] and not vis[i-1]:
                continue
            vis[i] = 1
            temp += str_temp[i]
            self.recursion(res,str_temp,temp,vis)
            vis[i] = 0
            temp = temp[:-1]