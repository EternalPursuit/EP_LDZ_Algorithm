
#
# visited = [False]*10
# minvalue = float("inf")
# def DFS(nums,visited,path):

allOfBody_scores_nums = [int(item) for item in input().split()]
sorted_allOfBody_scores_nums = sorted(allOfBody_scores_nums)

print(sorted_allOfBody_scores_nums)

diff_dp = [0] * 10
for i in range(10):
    diff_dp[i] = abs(sum(sorted_allOfBody_scores_nums[:i + 1]) - sum(sorted_allOfBody_scores_nums[i + 1:]))
index_min =  min(diff_dp)
index_min = diff_dp.index(index_min)


first_bodies_score_num = sorted_allOfBody_scores_nums[:index_min:2]

second_bodies_score_num = sorted_allOfBody_scores_nums[1:index_min:2]

first_bodies_score_num_last = sorted_allOfBody_scores_nums[index_min+1::2]
second_bodies_score_num_last = sorted_allOfBody_scores_nums[index_min::2]
print(first_bodies_score_num)
print("sec:",second_bodies_score_num)
print("last")
print(first_bodies_score_num_last)
print(second_bodies_score_num_last)
last_first = first_bodies_score_num_last +
# sorted_allOfBody_scores_nums = sorted(allOfBody_scores_nums)
#
# first_bodies_score_num = sorted_allOfBody_scores_nums[::2]
# print("first is : ",first_bodies_score_num)
# second_bodies_score_num = sorted_allOfBody_scores_nums[1::2]
# print(F"second is {second_bodies_score_num}")
# diff_of_two_nums = sum(first_bodies_score_num) - sum(second_bodies_score_num)
# print(abs(diff_of_two_nums))