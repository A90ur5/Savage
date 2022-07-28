from collections import defaultdict

class Solution:

    def heapSwim(self, heapTree, curNodeIndex):
        while curNodeIndex > 1 and heapTree[curNodeIndex][1] < heapTree[curNodeIndex >> 1][1]:
            parentsNodeIndex = curNodeIndex >> 1
            tmp = heapTree[curNodeIndex]
            heapTree[curNodeIndex] = heapTree[parentsNodeIndex]
            heapTree[parentsNodeIndex] = tmp
            curNodeIndex = parentsNodeIndex
        return heapTree

    def heapSink(self, heapTree, curNodeIndex):
        maxIndex = len(heapTree)
        leftChildIndex = curNodeIndex << 1
        rightChildIndex = (curNodeIndex << 1) + 1
        while rightChildIndex < maxIndex and heapTree[curNodeIndex][1] > min(heapTree[curNodeIndex << 1][1], heapTree[(curNodeIndex << 1) + 1][1]): 
            if heapTree[leftChildIndex][1] <= heapTree[rightChildIndex][1]: 
                #swap with left child
                tmp = heapTree[curNodeIndex]
                heapTree[curNodeIndex] = heapTree[leftChildIndex]
                heapTree[leftChildIndex] = tmp
                curNodeIndex = leftChildIndex
            else:
                if rightChildIndex > maxIndex:
                    break
                #swap with right child
                tmp = heapTree[curNodeIndex]
                heapTree[curNodeIndex] = heapTree[rightChildIndex]
                heapTree[rightChildIndex] = tmp
                curNodeIndex = rightChildIndex
            leftChildIndex = curNodeIndex << 1
            rightChildIndex = (curNodeIndex << 1) + 1

        if leftChildIndex == (maxIndex - 1) and heapTree[curNodeIndex][1] > heapTree[leftChildIndex][1]:
                tmp = heapTree[curNodeIndex]
                heapTree[curNodeIndex] = heapTree[leftChildIndex]
                heapTree[leftChildIndex] = tmp

        return heapTree

    def heapPopandInsert(self, heapTree, insertNode):
        heapTree[1] = insertNode
        heapTree = self.heapSink(heapTree, 1)
        return heapTree

    def zero(self):
        return 0

    #def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    def topKFrequent(self, nums, k):
        numsCounter = defaultdict(self.zero)
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            numsCounter[num] += 1
        #print(numsCounter)
        minHeap = [(0, 0)] * (k+1)
        i = 1
        for n, v in numsCounter.items():
            #print(minHeap)
            if i == k+1:
                if v > minHeap[1][1]:
                    minHeap = self.heapPopandInsert(minHeap, (n ,v))

            else:
                minHeap[i] = (n, v)
                minHeap = self.heapSwim(minHeap, i)
                i += 1
        res = [0]*k
        for i in range(k):
            res[i] = minHeap[i+1][0]

        return res


if __name__ == '__main__':
    ans = Solution()
    testData = [5,-3,9,1,7,7,9,10,2,2,10,10,3,-1,3,7,-9,-1,3,3]
    print(ans.topKFrequent(testData, 3))
