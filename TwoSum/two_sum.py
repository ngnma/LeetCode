def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        remain = target - num
        if seen.get(remain) is not None:
            return [i, seen[remain]]
        
        seen[num] = i

twoSum([2, 7, 11, 15], 9)