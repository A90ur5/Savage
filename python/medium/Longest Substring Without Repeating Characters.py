class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counterMap = [-1]*256

        maxLen = 0
        start = 0
        for i in range(len(s)):
            if counterMap[ord(s[i])] >= start:
                start = counterMap[ord(s[i])] + 1
            counterMap[ord(s[i])] = i
            maxLen = max(maxLen, i - start + 1)
        return maxLen
