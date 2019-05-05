class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        c =0
        for i, k in enumerate(reversed(A)):
            c += (ord(k) - 64)*(26**i)
        return c

    def convertToTitle(self, A):
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        col = ''
        while A>0:
            temp = A % 26
            if temp == 0:  temp, A = 26, A-1
            col = alpha[temp-1] + col
            A /= 26
        return col

if __name__ == '__main__':
    sol = Solution()
print sol.titleToNumber('BAA')
print sol.convertToTitle(1379)