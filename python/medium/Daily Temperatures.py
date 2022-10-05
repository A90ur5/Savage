class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and (temperatures[stack[-1]] < temperatures[i]):
                pi = stack.pop()
                res[pi] = i - pi

            stack.append(i)

        return res




if __name__ == '__main__':
    ans = Solution()
    testData = [30,40,50,60]
    print(ans.dailyTemperatures(testData))