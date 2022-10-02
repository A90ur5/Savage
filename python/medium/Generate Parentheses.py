class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def dfs(x: int, total: int, parenthesis: str):
            if total < n:
                dfs(x+1, total+1, parenthesis+'(')

            if x > 0:
                dfs(x-1, total, parenthesis+')')
            
            if total == n and x == 0:
                res.append(parenthesis)
            return

        dfs(0, 0, '')

        return res

if __name__ == '__main__':
    ans = Solution()
    testData = 3
    print(ans.generateParenthesis(testData))