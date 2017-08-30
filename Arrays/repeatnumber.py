

class Solution(object):
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        l, A = len(A), list(A)
        y = list(set(xrange(1, l + 1)) - set(A))

        for i in xrange(l):
            x = abs(A[i]) - 1
            if A[x] > 0:
                A[x] *= -1
            else:
                y.insert(0, abs(A[i]))
                break
        return y


if __name__ == '__main__':
    sol = Solution()
    print sol.repeatedNumber([3, 1, 1, 2])
