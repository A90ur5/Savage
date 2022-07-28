class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            elif not s[right].isalnum():
                right -= 1
                continue
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True

'''
    def neetcode_isalnum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
'''

'''
    def a_better_isalnum(c: str) -> bool:
        return (("a" <= c.lower() <= "z") or ("0" <= c <= "9"))
'''