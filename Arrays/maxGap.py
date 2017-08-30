

class Solution(object):
    # @param A : tuple of integers
    # @return an integer
    @staticmethod
    def get_ans(A, stack, index):
        _len, _value, rt = len(stack) - 1, A[index], -1
        while _len >= 0:
            if A[stack[_len]] <= _value:
                rt = index - stack[_len]
            else:
                return rt
            _len -= 1
        return rt

    def maximumGap(self, A):
        if not A or len(A) == 1:
            return 0
        stack, ans = [0], 0
        for i in range(1, len(A)):
            top = A[stack[-1]]
            if A[i] >= top:
                rt = self.get_ans(A, stack, i)
                ans = max(ans, rt)
            else:
                stack.append(i)
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.maximumGap([3, 5, 4, 2])
