from collections import Counter

class Solution:
    #def characterReplacement(self, s: str, k: int) -> int:
    def characterReplacement(self, s, k):
        l, r = 0, 0
        longest_substring = 0
        max_freq = 0
        word_counter = Counter()
        for r in range(len(s)):
            word_counter[s[r]] += 1
            max_freq = max(max_freq, word_counter[s[r]])
            while (r - l + 1) - max_freq > k:
                word_counter[s[l]] -= 1
                l += 1
                
            longest_substring = max(longest_substring, r -l + 1)
                
        return longest_substring

if __name__ == '__main__':
    ans = Solution()
    testData = "AABABBA"
    #testData = "ABAB"
    print(ans.characterReplacement(testData, 1))
