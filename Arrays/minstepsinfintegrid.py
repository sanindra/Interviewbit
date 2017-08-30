class Solution(object):
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        a, b = X[0], Y[0]
        c = 0
        for i in range(1, len(X)):
            c += max(abs(X[i] - a), abs(Y[i] - b))
            a, b = X[i], Y[i]

        return int(c)


if __name__ == '__main__':
    sol = Solution()
    print sol.coverPoints([0, 1, 1], [0, 1, 2])
