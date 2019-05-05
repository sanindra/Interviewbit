class Solution(object):
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        num, i = 0, 1
        while 5**i < A:
            num += A // (5**i)
            i +=1
        return  num

if __name__ == '__main__':
    sol = Solution()
print sol.trailingZeroes(100)