class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            one = 1
            two = 2
            for i in range(n-2):
                temp = two
                two = one + two
                one = temp
                
            return two



def main():
    mySol = Solution
    a = mySol.climbStairs(mySol, 38)
    #a = mySol.climbStairs(mySol, 3)
    print(a)

if __name__ == '__main__':
     main()