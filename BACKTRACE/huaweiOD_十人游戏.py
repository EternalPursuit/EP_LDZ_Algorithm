def findMinDifference(nums):
    total_num =sum(nums)
    min_diff = float('inf')

    def dfs(i,cur_sum):
        nonlocal min_diff
        if i == len(nums):
            other_sum = total_num - cur_sum
            min_diff = min(min_diff,abs(other_sum-cur_sum))
            return
        dfs(i+1,cur_sum+nums[i])
        dfs(i+1,cur_sum)
    dfs(0,0)
    return min_diff

nums = [1,2,3,4,5,6,7,8,9,10]
print(findMinDifference(nums))

def findMinDifference2(nums):
    total_num =sum(nums)
    min_diff = float('inf')
    best_group = None

    def dfs(i,group1,group2):
        nonlocal min_diff,best_group
        if i == len(nums):
            diff = abs(sum(group1) - sum(group2))
            if diff < min_diff:
                best_group = group1.copy()
                min_diff = diff
            return

        group1.append(nums[i])
        dfs(i+1,group1,group2)
        group1.pop()

        group2.append(nums[i])
        dfs(i+1,group1,group2)
        group2.pop()
    dfs(0,[],[])
    return best_group


nums = [1,2,3,4,5,6,7,8,9,10]
print(findMinDifference2(nums))

def findMinDifference3(nums):
    total_sum = sum(nums)
    min_diff = float('inf')
    best_group = None

    def backtrack(i,group1,group2):
        nonlocal min_diff,best_group
        if len(group1) == 5 and len(group2) == 5:
            diff =abs(sum(group1) - sum(group2))
            if diff < min_diff:
                min_diff = diff
                best_group = group1.copy()
            return

        if i == len(nums):
            return
        if len(group1) < 5:
            group1.append(nums[i])
            backtrack(i+1,group1,group2)
            group1.pop()

        if len(group2) < 5:
            group2.append(nums[i])
            backtrack(i+1,group1,group2)
            group2.pop()
    backtrack(0,[],[])
    return  best_group


nums = [1,2,3,4,5,6,7,8,9,10]
print(findMinDifference3(nums))


def findMinDifference4(nums):
    total_sum = sum(nums)
    min_diff = float('inf')
    best_group = None

    def backtrack(i,group1):
        nonlocal min_diff,total_sum,best_group
        if len(group1) == 5:
            diff = abs(2*sum(group1)-total_sum)
            if diff < min_diff:
                min_diff = diff
                best_group = group1.copy()
            return
        if i == len(nums):
            return
        group1.append(nums[i])
        backtrack(i+1,group1)
        group1.pop()

        backtrack(i+1,group1)

    backtrack(0,[])

    return  best_group
nums = [1,2,3,4,5,6,7,8,9,10]
print(findMinDifference4(nums))
