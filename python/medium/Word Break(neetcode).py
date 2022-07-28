class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lenS = len(s)
        dp = [False] * (lenS + 1)
        dp[lenS] = True
        for i in range(lenS-1, -1, -1):
            for word in wordDict:
                lenW = len(word)
                if lenW + i <= lenS and word == s[i:i+lenW]:
                    dp[i] = dp[i+lenW]

                if dp[i]:
                    break
        return dp[0]