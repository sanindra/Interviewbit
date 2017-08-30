

class Solution(object):
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        return [self.generateRows(i) for i in xrange(A)]
    
    def generateRows(self, n):
        row = [0 for _ in xrange(n+1)]
        row[0], row[-1] = 1, 1
        
        for i in xrange(n/2):
            y = row[i]*(n-i)/(i+1)
            row[i+1], row[n-i-1] = y, y
        return row

if __name__ == '__main__':
    sol = Solution()
    print sol.generate(5)
