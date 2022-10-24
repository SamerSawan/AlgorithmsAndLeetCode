def containsDuplicate(nums):

    s = set()

    for n in nums:
        if n in s:
            return True
        s.add(n)
    return False


# driver code to test solution

print(containsDuplicate([1, 2, 3, 4]))
# Expected output: False

print(containsDuplicate([1, 2, 2, 4]))
# Expected output: True

print(containsDuplicate([1, 2, 3, 2]))
# Expected output: True

