

class Solution(object):
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        row =[0 for i in xrange(A+1)]
        row[0], row[-1] = 1, 1
        
        for i in xrange(A/2):
            x = row[i]*(A-i)/(i+1)
            row[i+1], row[A-1-i] = x, x
        return row

if __name__ == '__main__':
    sol = Solution()
    print sol.getRow(3)
