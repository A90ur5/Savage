class Solution:
    DParray = {}
    def climbStep(self, stair, top):
        if stair == top:
            return 1
        elif stair > top:
            return 0
        else:
            if stair + 1 in self.DParray:
                step1 = self.DParray[stair+1]
            else:
                step1 = self.climbStep(self, stair + 1, top)
                self.DParray[stair+1] = step1

            if stair + 2 in self.DParray:
                step2 = self.DParray[stair+2]
            else:
                step2 = self.climbStep(self, stair + 2, top)
                self.DParray[stair+2] = step2

            return step1 + step2

    def climbStairs(self, n: int) -> int:
        return self.climbStep(self, 0, n)

def main():
    mySol = Solution
    #a = mySol.climbStairs(mySol, 38)
    a = mySol.climbStairs(mySol, 3)
    print(a)

if __name__ == '__main__':
     main()

'''
version which submitted to leetcode
class Solution:
    def climbStairs(self, n: int) -> int:
        self.DParray = {}
        def climbStep(stair, top):
            if stair == top:
                return 1
            elif stair > top:
                return 0
            else:
                if stair + 1 in self.DParray:
                    step1 = self.DParray[stair+1]
                else:
                    step1 = climbStep(stair + 1, top)
                    self.DParray[stair+1] = step1

                if stair + 2 in self.DParray:
                    step2 = self.DParray[stair+2]
                else:
                    step2 = climbStep(stair + 2, top)
                    self.DParray[stair+2] = step2

                return step1 + step2
        return climbStep(0, n)
'''