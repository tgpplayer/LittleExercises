# Program that returns the two indices of the two numbers of a list that sum a target.

nums = [3, 5, 8, 1]
target = 4

def indices_that_sum_target(nums, target):
    for i in range(len(nums)):
        p_second_num = target - nums[i]
        if p_second_num in nums:
            return i, nums.index(p_second_num)

first_index = indices_that_sum_target(nums, target)[0]
second_index = indices_that_sum_target(nums, target)[1]

print(f"The indices that sum the target {target} are {first_index} and {second_index}")
