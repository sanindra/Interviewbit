
class Solution(object):
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        if A == 1:
            return True

        for i in xrange(2, int(A ** 0.5) + 1):
            y = 2
            p = i ** y
            while A >= p > 0:
                if p == A:
                    return True
                y += 1
                p = i ** y
        return False

if __name__ == '__main__':
    sol = Solution()
    print sol.isPower(16)
