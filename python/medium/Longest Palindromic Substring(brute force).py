class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen_L = 0
        maxLen_R = 0
        maxLen = 0
        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                localLen = r - l + 1
                if localLen > maxLen:
                    maxLen = localLen
                    maxLen_L = l
                    maxLen_R = r

            #even
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                localLen = r - l + 1
                if localLen > maxLen:
                    maxLen = localLen
                    maxLen_L = l
                    maxLen_R = r

                l -= 1
                r += 1

        return s[maxLen_L:maxLen_R]