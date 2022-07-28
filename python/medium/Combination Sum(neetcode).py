#neetcode solution
#using append() & pop() to maintain the curSet
#It seems slower than pass a copy of curSet to subTree
#but it's more intuitive

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        maxIndex = len(candidates) - 1
        candidates.sort()

        def dfs(index, curSum, curSet):
            if curSum == target:
                res.append(curSet.copy())
                return

            elif curSum > target or index > maxIndex:
                return            

            else:
                #go left subtree
                curSet.append(candidates[index])
                dfs(index, curSum + candidates[index], curSet)
                curSet.pop()

                #go right subtree
                dfs(index + 1, curSum, curSet)
                return

        dfs(0, 0, [])
        return res