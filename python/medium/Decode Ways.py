class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s) : 1 }

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0

            left = dfs(i+1)            
            if i+2 <= len(s) and (s[i] == '1' or \
                s[i] == '2' and s[i+1] in "0123456"):
                right = dfs(i+2)
            else:
                right = 0
            dp[i] = left + right
            return dp[i]

        return dfs(0)