class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        matrix = [[0 for _ in xrange(A)] for _ in xrange(A)]
        
        l, r, t, b, n = 0, A-1, 0, A-1, 1
        while l<=r and t<=b:
            for j in xrange(l,r+1):
                matrix[t][j] = n
                n+=1
            
            for j in xrange(t+1,b):
                matrix[j][r] = n
                n+=1
            
            for j in reversed(xrange(l, r+1)):
                if t<b:
                    matrix[b][j] = n
                    n+=1
            
            for j in reversed(xrange(t+1,b)):
                if l<r:
                    matrix[j][l] = n
                    n+=1
            l, r, t, b = l+1, r-1, t+1, b-1
        
        return matrix
if __name__ == '__main__':
    sol = Solution()
    print sol.generateMatrix(3)