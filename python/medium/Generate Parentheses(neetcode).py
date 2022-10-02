class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        stack = []
        def backtrack(open_parenthesis: int, close_parenthesis: int):
            if open_parenthesis == close_parenthesis == n:
                res.append(''.join(stack))

            if open_parenthesis < n:
                stack.append('(')
                backtrack(open_parenthesis + 1, close_parenthesis)
                stack.pop()

            if close_parenthesis < open_parenthesis:
                stack.append(')')
                backtrack(open_parenthesis, close_parenthesis + 1)
                stack.pop()
            
            return

        backtrack(0, 0)
        
        return res

if __name__ == '__main__':
    ans = Solution()
    testData = 3
    print(ans.generateParenthesis(testData))