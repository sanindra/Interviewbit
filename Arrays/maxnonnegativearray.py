class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        if len(A) == 0:
            return 0
        maxSum = max(A[0], 0)
        self.l, a, temp = {}, [], 0
        
        for i in A:
            if i >= 0:
                maxSum += i
                a.append(i)
            else:
                self.populateDict(maxSum, a)
                a = [i] if i>=0 else []
                maxSum = 0

        if maxSum: self.populateDict(maxSum, a)
        m = max(self.l) if self.l else -1
        
        return self.l[m] if m!=-1 else []
    
    def populateDict(self, maxSum, a):
        if maxSum in self.l:
            if len(self.l[maxSum]) < len(a):
                self.l[maxSum] = a
        else:
            self.l[maxSum] = a

if __name__ == '__main__':
    sol = Solution()
    print sol.maxset([1, 2, 5, -7, 2, 3])