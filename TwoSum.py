def twoSum(nums, target):
    prevMap = {}

    for i, n in enumerate(nums):
        temp = target - n
        if temp in prevMap:
            return [prevMap[temp], i]
        prevMap[n] = i


# driver code to test solution

print(twoSum([2, 7, 11, 15], 9))
# Expected output: [0,1]

print(twoSum([1, 2, 3, 4], 5))
# Expected output: [1,2]

print(twoSum([3, 5, 8, 11], 14))
# Expected output: [0,3]

print(twoSum([0, 3, 4, 7], 7))
# Expected output: [1,2]
