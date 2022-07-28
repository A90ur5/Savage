class Solution:
    #def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    def wordBreak(self, s, wordDict) -> bool:
        lenS = len(s)
        global dp
        global res
        res = False
        dp = [True] * lenS
        def dfs(i):
            global res
            if i == lenS:
                return True
            elif dp[i] == False:
                return False
                
            for word in wordDict:
                n = len(word)
                if i + n > lenS:
                    continue
                if s[i:i+n] == word:
                    res = (res or dfs(i+n))
                    if res:
                        break
                dp[i] = False
            return res

        return dfs(0)


if __name__ == '__main__':
    ans = Solution()
    testData = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    testData2 = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print(ans.wordBreak(testData, testData2))

