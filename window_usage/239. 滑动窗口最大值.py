# import heapq
# heap = []
#
# heapq.heappush(heap,10)
# heapq.heappush(heap,1)
# heapq.heappush(heap,5)
#
# # 从堆中弹出最小的元素
# smallest = heapq.heappop(heap)
# print(smallest)
# # 查看堆的最小值
# smallest = heap[0]
#
# # 将列表转换为堆,是在list1上原地操作的。
# # 结果：the list1 after heapify is :  [1, 2, 3, 7, 6, 8, 5, 44, 10]
# list1 = [10,1,5,2,6,8,3,44,7]
# heapq.heapify(list1)
# print("the list1 after heapify is : ",list1)
#
# # 使用堆来获取最大的n个元素，或最小的n个元素
# print(heapq.nsmallest(2,list1))
# print(heapq.nlargest(2,list1))
import heapq


def maxSLidingWindow(nums,k):
    n = len(nums)
    q = [(-nums[i],i) for i in range(k)]
    heapq.heapify(q)
    ans = [-q[0][0]]
    for i in range(k,n):
        heapq.heappush(q,(-nums[i],i))
        while q[0][1] <= i-k:
            heapq.heappop(q)
        ans.append(-q[0][0])
    return ans


