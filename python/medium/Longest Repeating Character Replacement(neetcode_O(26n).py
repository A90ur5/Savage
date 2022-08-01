from collections import Counter

class Solution:
    #def characterReplacement(self, s: str, k: int) -> int:
    def characterReplacement(self, s, k):
        l, r, res = 0, 0, 0
        word_counter = Counter()

        for i in range(len(s)):
            r = i
            word_counter[s[r]] += 1
            
            while (r - l + 1) - max(word_counter.values()) > k:
                word_counter[s[l]] -= 1
                l += 1                

            res = max(r-l+1, res)
        return res

if __name__ == '__main__':
    ans = Solution()
    #testData = "AABABBA"
    testData = "ABAA"
    print(ans.characterReplacement(testData, 0))
