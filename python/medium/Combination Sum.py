class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        maxIndex = len(candidates) - 1
        candidates.sort()
        def dfs(index, curSum, curSet):
            nextSum = curSum + candidates[index]

            if nextSum < target:
                #go right
                if index+1 <= maxIndex:
                    dfs(index+1, curSum, curSet)
                #go left
                curSet.append(candidates[index])
                dfs(index, nextSum, curSet.copy())
                return

            elif nextSum == target:
                curSet.append(candidates[index])
                res.append(curSet)
                return

            else:
                return

        dfs(0, 0, [])
        return res