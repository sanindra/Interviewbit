import math

class Solution(object):
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        if A>1:
            def isPrime(num):
                for i in xrange(2, int(math.sqrt(num+1))):
                    if num % i == 0: return 0
                return 1
            for i in xrange(2, A+1):
                if isPrime(i) and A-i >=i and isPrime(A-i):
                    return [i, A-i]
        return []


if __name__ == '__main__':
    sol = Solution()
    print sol.primesum(16)


