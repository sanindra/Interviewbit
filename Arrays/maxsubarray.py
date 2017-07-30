class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
    	max1, max2 = 0, 0

    	for i in A:
    		max1+=i
    		if max1<0: max1=0
    		max2 = max(max1, max2)

    	return max2 if max2 else max(A)


if __name__ == '__main__':
    sol = Solution()
    print sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])