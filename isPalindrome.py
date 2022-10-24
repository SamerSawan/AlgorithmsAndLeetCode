def isPalindrome(s):

    tmp = ""

    for c in s:
        if c.isalnum():
            tmp += c.lower()

    return tmp == tmp[::-1]

#driver code to test function

print(isPalindrome("race a car"))
# Expected output: False

print(isPalindrome("racecar"))
# Expected output: True

print(isPalindrome("rotor"))
# Expected output: True

print(isPalindrome("saippuakivikauppias"))
# Expected output: True


