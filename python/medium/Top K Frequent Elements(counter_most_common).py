# Source: 
# https://leetcode.com/problems/top-k-frequent-elements/discuss/81639/1-line-Python-Solution-using-Counter-with-explanation/180490

import collections
class Solution(object):
    #def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    def topKFrequent(self, nums, k):
        return [k for k, v in collections.Counter(nums).most_common(k)]


if __name__ == '__main__':
    ans = Solution()
    testData = [3,0,1,0]
    print(ans.topKFrequent(testData, 1))
