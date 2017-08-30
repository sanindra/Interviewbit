

class Solution(object):
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        A = list(A)
        n = len(A)
        if n < 2:
            return 0
        A.sort()
        m = A[1]-A[0]
        for i in xrange(1, n-1):
            m = max(m, A[i+1]-A[i])
        return m

if __name__ == '__main__':
    sol = Solution()
    print sol.maximumGap([1, 10, 5])
