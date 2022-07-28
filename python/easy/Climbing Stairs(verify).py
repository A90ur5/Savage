class Solution:
    def climbStairs(self, n: int) -> int:
        a = n
        res = 0
        m = 0
        n = 1        
        for i in range(1, a+1):
            s = m + n
            res = s
            m = n
            n = s
        return res

def main():
    mySol = Solution
    a = mySol.climbStairs(mySol, 38)
    print(a)

if __name__ == '__main__':
     main()
