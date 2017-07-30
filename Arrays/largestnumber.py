class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        return ''.join(sorted(map(str, A), cmp=self.compare, reverse=True))
    
    def compare(self, x, y):
        return int(x+y)-int(y+x)


if __name__ == '__main__':
    sol = Solution()
    print sol.largestNumber([3, 30, 34, 5, 9])