class Solution:
    def climbStep(self, stair, top):
        if stair == top:
            return 1
        elif stair > top:
            return 0
        else:
            step1 = self.climbStep(self, stair + 1, top)
            step2 = self.climbStep(self, stair + 2, top)
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
