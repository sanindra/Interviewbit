

class Solution(object):
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        A = list(A)
        for i in xrange(len(A)):
            x = abs(A[i])-1
            if A[x] > 0:
                A[x] *= -1
            else:
                return abs(A[i])
        return -1


if __name__ == '__main__':
    sol = Solution()
    print sol.repeatedNumber([3, 1, 1, 2])